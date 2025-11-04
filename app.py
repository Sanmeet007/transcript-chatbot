from dotenv import load_dotenv

load_dotenv(".env")

from fastapi import FastAPI, Response, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.model import GeminiModel as model
from utils.transcript_loader import fetch_transcript, TranscriptsDisabled
from utils.vector_store import get_retriever, get_store, Chroma
from utils.prompts import prompt, get_initial_chat_history
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from uuid import uuid4
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

sessions = {}


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/session/start")
def start_session(response: Response):
    session_id = str(uuid4())
    sessions[session_id] = {
        "messages": get_initial_chat_history(),
        "vector_store": None,
    }
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        samesite="Lax",
        max_age=60 * 60 * 2,  # 2 hours
    )
    return {"message": "Session started"}


@app.delete("/session/end")
def end_session(request: Request, response: Response):
    session_id = request.cookies.get("session_id")
    if session_id in sessions:
        del sessions[session_id]
    response.delete_cookie("session_id")
    return {"message": "Session ended"}


@app.post("/load")
def load(request: Request, video_id: str):
    try:
        session_id = request.cookies.get("session_id")
        session = sessions.get(session_id)

        if not session:
            return {"error": "Invalid session"}

        transcript = fetch_transcript(video_id)
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )
        docs = splitter.create_documents([transcript])

        if session["vector_store"]:
            session["vector_store"].delete_collection()
        else:
            session["vector_store"] = get_store()

        store: Chroma = session["vector_store"]
        store.add_documents(docs)

        return {"message": "Transcript loaded successfully"}
    except TranscriptsDisabled:
        return {"message": "Unable to load transcript"}


from pydantic import BaseModel


class AskRequest(BaseModel):
    query: str


@app.post("/ask")
def ask(request: Request, data: AskRequest):
    query = data.query
    session_id = request.cookies.get("session_id")
    session = sessions.get(session_id)

    if not session:
        return {"error": "Invalid session"}

    if not session["vector_store"]:
        return {"error": "load video first"}

    retriever = get_retriever(session["vector_store"])

    context_docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in context_docs])

    chain = prompt | model | StrOutputParser()

    session["messages"].append(HumanMessage(content=query))
    result = chain.invoke(
        {
            "question": query,
            "context": context,
            "chat_history": session["messages"],
        }
    )
    session["messages"].append(AIMessage(content=result))

    return {"response": result}  # type: ignore


if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload=True)
