# 🎬 Transcript Chatbot

**Transcript Chatbot** is a lightweight **Retrieval-Augmented Generation (RAG)** web application that enables users to **interact conversationally with YouTube video transcripts**.  
By fetching, embedding, and retrieving transcript data from a **Chroma Vector Store**, the system allows users to ask natural questions and receive **contextually relevant, human-like responses**.

---

## 🚀 Key Features
- **🎥 Transcript Integration:** Load and process YouTube video transcripts seamlessly.  
- **💬 Conversational AI:** Generates natural, context-aware answers without rigid phrasing.  
- **🧠 RAG Architecture:** Combines retrieval and generation for accurate, grounded responses.  
- **💾 Chroma Vector Store:** Efficiently stores and retrieves transcript embeddings for fast similarity search.  
- **🌙 Modern UI:** Clean, responsive, dark-themed interface with typing indicators.  
- **⚡ Real-Time Interaction:** Smooth and fast chat experience powered by **FastAPI** and **Uvicorn**.  


## 📸 Screenshots 

![Screenshot-1](https://sanmeet007.github.io/public/transcript-chatbot/screenshot-1.png)
![Screenshot-2](https://sanmeet007.github.io/public/transcript-chatbot/screenshot-2.png)
![Screenshot-3](https://sanmeet007.github.io/public/transcript-chatbot/screenshot-3.png)
![Screenshot-4](https://sanmeet007.github.io/public/transcript-chatbot/screenshot-4.png)
---

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python (FastAPI) |
| **AI Layer** | Gemini / LangChain with text embeddings |
| **Vector Database** | ChromaDB |
| **Storage** | In-memory session management |
| **Deployment** | Uvicorn web server |

---

## 🧩 System Overview
1. **Session Initialization:** Creates a temporary session to manage chat state.  
2. **Transcript Loading:** Retrieves and processes YouTube transcripts, splitting them into chunks.  
3. **Embedding & Storage:** Generates embeddings and stores them in **Chroma Vector Store**.  
4. **Question Answering (RAG):** On each query, relevant transcript chunks are retrieved from Chroma and passed to the model for answer generation.  
5. **Session Termination:** Sessions and embeddings are automatically cleared upon exit.  

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/transcript-chatbot.git
cd transcript-chatbot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
uvicorn app:app --reload
```

### 4️⃣ Access the Web Interface

Open your browser and navigate to:

```
http://localhost:8000
```

---

## 🧾 Environment Variables

Create a `.env` file with the following configuration:

```bash
GOOGLE_API_KEY=your_gemini_api_key
```
