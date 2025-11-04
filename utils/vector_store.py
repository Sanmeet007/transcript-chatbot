from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def get_store():
    store = Chroma(
        embedding_function=GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001",
        )
    )
    return store


def get_retriever(store):
    retriever = store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 4,
        },
    )
    return retriever
