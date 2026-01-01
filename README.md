

---

# 🧩 AI-Powered Web App / Game Generator using Streamlit & Google Gemini

This project is a **Streamlit-based AI application generator** built using **LangChain** and **Google Gemini (gemini-2.5-flash)**.
It allows users to **describe a web app or game**, and the AI automatically **generates and runs a full Python application**.

Special handling is included for **games and calculators**, which are launched in a **Pygame popup window**.

---

## 📌 Features

* Interactive UI built with **Streamlit**
* Uses **Google Gemini** via **LangChain**
* Accepts **natural language descriptions**
* Automatically generates **complete Python applications**
* Supports:

  * Web-style Python apps
  * Games & calculators using **Pygame**
* Secure API key handling with **dotenv**
* Supports **user-provided API key** or `.env` fallback
* Auto-runs generated application

---

## 🧠 How the Code Works

### 1️⃣ Page Configuration

```python
st.set_page_config(
    page_title="AI Web/Game Generator",
    page_icon="🧩",
    layout="centered"
)
```

* Sets app title, icon, and layout
* Improves UI consistency

---

### 2️⃣ Environment Setup

```python
load_dotenv()
```

* Loads environment variables from `.env`
* Keeps API keys **secure and configurable**

---

### 3️⃣ Sidebar Instructions & API Key Input

```python
user_api_key = st.sidebar.text_input(
    "🔑 Enter your Gemini API Key",
    type="password"
)
```

* Allows users to enter their **own Gemini API key**
* Falls back to `.env` key if not provided
* Sidebar clearly explains **how to use the app**

---

### 4️⃣ LLM Initialization

```python
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)
```

* Initializes **Google Gemini Flash model**
* `temperature=0` ensures **deterministic, clean code output**
* LangChain acts as a **client**
* Gemini acts as a **closed-source LLM server**

---

### 5️⃣ Prompt Engineering (Core Logic)

```python
prompt = [
    ("system", "...RULES..."),
    ("user", user_prompt)
]
```

**System Rules Enforced:**

* Output **ONLY Python code**
* No markdown, comments, or explanations
* If request contains:

  * `game`
  * `calculator`
    ➜ MUST use **pygame** and open a popup window

This ensures **valid, runnable applications**.

---

### 6️⃣ Code Generation & Execution Flow

```
User Description
      ↓
System Rules + Prompt
      ↓
Gemini via LangChain
      ↓
Pure Python Code
      ↓
Saved as appp.py
      ↓
Executed Automatically
```

---

### 7️⃣ Code Cleanup & Execution

````python
code = re.sub(r"```python|```", "", code).strip()
subprocess.Popen([sys.executable, file_path])
````

* Removes markdown fences if Gemini adds them
* Saves output as `appp.py`
* Automatically runs the generated app
* Opens **Pygame window** for games/calculators

---

## 📦 Dependencies

### `requirements.txt`

```txt
streamlit
langchain
langchain_google_genai
python-dotenv
```

### Why These Dependencies?

| Package                | Purpose                   |
| ---------------------- | ------------------------- |
| streamlit              | UI for the generator      |
| langchain              | LLM abstraction           |
| langchain_google_genai | Google Gemini integration |
| python-dotenv          | Secure API key handling   |

---

## 🔐 Why Use `dotenv`?

* Keeps API keys **out of source code**
* Prevents accidental leaks on GitHub
* Allows different keys for **local & production**
* Supports fallback when user does not provide key

### Example `.env` File

```env
gem=YOUR_GOOGLE_GEMINI_API_KEY
```

---

## 🚫 Why Use `.gitignore`?

Prevents sensitive and unnecessary files from being pushed.

### `.gitignore`

```gitignore
.env
__pycache__/
venv/
.env.local
```

✅ Protects API keys
✅ Keeps repository clean
✅ Follows industry best practices

---

## 🚀 Run Locally (Step-by-Step)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-web-game-generator.git
cd ai-web-game-generator
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add `.env` File (Optional)

```env
gem=YOUR_GEMINI_API_KEY
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push project to **GitHub**
2. Open **Streamlit Cloud**
3. Select your repository
4. Add Environment Variable:

   ```
   gem = YOUR_GEMINI_API_KEY
   ```
5. Deploy 🚀

---

## 📜 MIT License

```text
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```

---

## 📚 Learning Outcomes

* Prompt-driven application generation
* LangChain with closed-source LLMs
* Gemini Flash model usage
* Streamlit UI + sidebar UX
* Secure API handling
* Dynamic code execution
* Pygame automation

---

## 🙌 Author

**Aashish**
AI / ML / GenAI Developer

---
