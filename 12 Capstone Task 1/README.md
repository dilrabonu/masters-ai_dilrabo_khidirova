# 🤖 Intelligent AI Assistants for Domain-Specific Support  
**Capstone: LangChain + RAG | AutoSupport-AI on Hugging Face**

Welcome to my project repository for two powerful AI Assistants developed for real-world domain-specific query resolution. These projects leverage state-of-the-art technologies like OpenAI GPT, LangChain, FAISS, and Hugging Face Spaces to deliver intelligent, scalable, and accurate assistant solutions.

---

## 🚗 AutoSupport-AI – Automotive Support Assistant (Hugging Face Deployment)

A live, interactive chatbot that provides intelligent responses to vehicle-related inquiries using OpenAI GPT and document retrieval through FAISS.

🔗 **Live Demo:** [AutoSupport-AI on Hugging Face](https://huggingface.co/spaces/Dilrabonu/Auto-Support-AI)

### ✨ Features
- Built using **OpenAI GPT models**
- Custom vehicle manual ingestion using **FAISS vector search**
- Responsive **chat interface** powered by `streamlit`
- Designed to support vehicle troubleshooting, tire recommendations, and general automotive queries
- Secure **API key session management** for runtime usage

---

## 🎓 Capstone AI Assistant – LangChain + RAG

An intelligent assistant built as part of a capstone project, utilizing **LangChain**, **RAG pipelines**, and **embeddings** to support high-precision knowledge retrieval from custom document sources.

### ✨ Features
- Integrated **LangChain memory and prompts** for context-aware conversations
- **RAG (Retrieval-Augmented Generation)** for grounded answers
- **FAISS**-powered semantic vector search over domain-specific knowledge bases
- Ideal for **educational tutors**, **enterprise FAQs**, or **internal documentation assistants**

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🧠 OpenAI GPT | Natural Language Generation |
| 🔗 LangChain | Agent chains, prompt templates, memory |
| 📚 FAISS | Vector storage for document embeddings |
| 🧰 Hugging Face Spaces | Deployment of AutoSupport-AI with `streamlit` |
| 🐍 Python | Core language for backend and integrations |
| 🧠 SentenceTransformers | Text embedding generation |
| 🌐 Streamlit | Web-based user interface |

---

## 📂 Repository Structure

```bash
├── app.py                   # Main app for Hugging Face deployment
├── chat_handler.py         # Message processing and response generation
├── document_processor.py   # Document loading and embedding logic
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── data/                   # Source documents (manuals, FAQs)
├── faiss_index/            # FAISS vector store






🚀 Setup Instructions
1. Clone the Repo

git clone https://github.com/yourusername/ai-support-assistants.git
cd ai-support-assistants

Install Dependencies
pip install -r requirements.txt

Add Your API Key

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


Run app locally

streamlit run app.py


📬 Contact
For collaboration, questions, or feedback:

Dilrabo Khidirova
📧 dilrabo_khidirova@epam.com
🔗 (https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/)
