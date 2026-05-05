
import os
from fastapi import FastAPI
from groq import Groq # <--- Use the real Groq library

app = FastAPI()

# No more base_url needed, it knows where to go
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.get("/")
def read_root():
    return {"message": "Groq Chatbot Online"}

@app.post("/chat")
def chat(prompt: str):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}

