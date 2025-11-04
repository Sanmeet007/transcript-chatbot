# 🎬 Transcript Chatbot

**Transcript Chatbot** is a lightweight web application that enables users to **interact conversationally with YouTube video transcripts**.  
By fetching and embedding transcript data, the system allows users to ask natural questions and receive contextually relevant, human-like responses.

---

## 🚀 Key Features
- **🎥 Transcript Integration:** Load YouTube video transcripts seamlessly.  
- **💬 Conversational AI:** Natural, context-aware responses without rigid phrasing.  
- **🧠 Contextual Retrieval:** Uses embeddings to identify the most relevant transcript segments.  
- **🌙 Modern UI:** Clean, responsive, dark-themed interface with typing indicators.  
- **⚡ Real-Time Interaction:** Fast and smooth chat experience powered by FastAPI.  

---

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python (FastAPI) |
| **AI Layer** | Gemini / LangChain integration with text embeddings |
| **Storage** | In-memory session management |
| **Deployment** | Uvicorn web server |

---

## 🧩 System Overview
1. **Session Initialization:** Creates a temporary session to manage chat state.  
2. **Transcript Loading:** Retrieves and processes YouTube transcripts, splitting them into text chunks.  
3. **Question Answering:** The model uses similarity search on embeddings to find relevant context and generates a conversational answer.  
4. **Session Termination:** Sessions and related embeddings are automatically cleared upon exit.  

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/transcript-chatbot.git
cd transcript-chatbot
````

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