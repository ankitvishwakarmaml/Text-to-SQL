# Text-to-SQL
A production-ready Text-to-SQL application using LangChain, Groq LLM, Streamlit, and ChromaDB. This project allows users to input natural language queries and converts them into SQL queries, which are then executed on an SQLite database.
---

## 🚀 Getting Started

### **1️⃣ Clone the Repository**
```bash
git clone [https://github.com/ankitvishwakarmaml/Text-to-SQL.git]
cd Text-to-SQL
```

### **2️⃣ Install UV Package Manager**
```bash
pip install uv
```

### **3️⃣ Create environment using UV**
```bash
uv python install 3.11
uv .venv/bin/activate
```

### **4️⃣ Install Dependencies using UV**
```bash
uv sync
```
OR, if using `pyproject.toml`:
```bash
uv pip install
```

### **5️⃣  Set Up Environment Variables**
Create a `.env` file and add your **Groq API Key**:
```ini
GROQ_API_KEY=your_groq_api_key
```

---

## 🔥 Features
- **Natural Language to SQL** conversion using LangChain and Groq LLM.
- **Vector Storage** with ChromaDB for efficient query retrieval.
- **Streamlit UI** for user-friendly interaction.
- **FastAPI API Endpoints** for integration with other applications.
- **Lightweight Dependency Management** with UV package manager.

---

## 🛠️ Contributing
Feel free to fork the repo, make changes, and submit a pull request! 🚀

---

## 📜 License
This project is licensed under the **MIT License**. See `LICENSE` for details.

---

## ✨ Acknowledgments
- [LangChain](https://github.com/hwchase17/langchain)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Streamlit](https://github.com/streamlit/streamlit)
- [Uvicorn](https://github.com/encode/uvicorn)
- [UV Package Manager](https://github.com/astral-sh/uv)

---

🔗 **Connect with me on GitHub:** [ankitvishwakarmaml](https://github.com/ankitvishwakarmaml) 🚀

