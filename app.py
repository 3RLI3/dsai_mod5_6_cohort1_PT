#gemini
import os
from flask import Flask, request, render_template
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env (for local dev)
load_dotenv()

# Securely configure the Gemini API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY environment variable")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/gemini", methods=["GET", "POST"])
def gemini():
    return render_template("gemini.html")

@app.route("/gemini_reply", methods=["GET", "POST"])
def gemini_reply():
    q = request.form.get("q")
    print(f"User query: {q}")
    r = model.generate_content(q)
    return render_template("gemini_reply.html", r=r.text)

if __name__ == "__main__":
    app.run(debug=True)
