import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
import subprocess
import sys
import re
import time

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Web/Game Generator",
    page_icon="🧩",
    layout="centered"
)

# -----------------------------
# Load Environment
# -----------------------------
load_dotenv()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🛠️ How to Use This App")

st.sidebar.markdown("""
### Steps:
1. Enter your **Gemini API Key** (optional)
2. Describe the app or game you want
3. Click **Generate App**
4. Wait while the AI builds it
5. A new window will open automatically

### Special Rules:
- If your request contains:
  - **calculator**
  - **game**
  
  ➜ The app will open in a **Pygame popup window**
""")

user_api_key = st.sidebar.text_input(
    "🔑 Enter your Gemini API Key",
    type="password",
    placeholder="AIza..."
)

# Use user key or fallback to .env
if user_api_key:
    os.environ["GOOGLE_API_KEY"] = user_api_key
else:
    os.environ["GOOGLE_API_KEY"] = os.getenv("gem")

# -----------------------------
# Main UI
# -----------------------------
st.title("🧩 AI-Powered Web App / Game Generator")

st.write("""
**Example Inputs:**
- Create a calculator  
- Build a small game  
- Make a task manager app  

⚠️ *Games and calculators always launch in a Pygame window.*
""")

user_prompt = st.text_area(
    "Enter your app/game description",
    height=120
)

# -----------------------------
# Model
# -----------------------------
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# -----------------------------
# Generate App
# -----------------------------
if st.button("🚀 Generate App"):

    if not user_prompt.strip():
        st.warning("Please enter a description.")
        st.stop()

    prompt = [
        (
            "system",
            """
You are an AI that generates FULL Python applications.

RULES:
1. Output ONLY Python code.
2. No explanations, comments, or markdown.
3. If the request contains "game" or "calculator":
   - MUST use pygame
   - MUST open a pygame popup window
4. Otherwise generate a normal Python application.
            """
        ),
        ("user", user_prompt)
    ]

    start_time = time.time()

    with st.spinner("⏳ Generating application... Please wait"):
        output = model.invoke(prompt)
        elapsed = round(time.time() - start_time, 2)

    code = output.content

    # Remove markdown fences if any
    code = re.sub(r"```python|```", "", code).strip()

    file_path = "appp.py"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)

    st.success(f"✅ App generated successfully in {elapsed} seconds!")

    try:
        subprocess.Popen([sys.executable, file_path])
        st.info("🖥️ If it’s a game or calculator, a Pygame window will appear.")
    except Exception as e:
        st.error(f"❌ Error running generated app: {e}")
