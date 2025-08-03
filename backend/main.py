from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import json
import requests
import os
from typing import Optional

app = FastAPI()

# CORS setup for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY', 'your-api-key-here')
USE_OPENROUTER = True  # Set to False to use local Ollama

async def call_openrouter(user_msg: str, system_prompt: str) -> str:
    """Call OpenRouter API for AI response"""
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3.1-8b-instruct",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_msg}
                ]
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            return f"OpenRouter API error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Error calling OpenRouter: {str(e)}"

async def call_local_ollama(user_msg: str, system_prompt: str) -> str:
    """Call local Ollama API for AI response"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"{system_prompt}\n\nUser: {user_msg}\n\nBrampton:",
                "stream": False
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "Sorry, I couldn't process that request.")
        else:
            return "Sorry, I'm having trouble connecting to the local Ollama model. Please make sure Ollama is running."
            
    except Exception as e:
        return f"Error: {str(e)}. Please ensure Ollama is running on localhost:11434"

@app.post("/api/chat")
async def chat(req: Request):
    data = await req.json()
    user_msg = data.get("message")

    system_prompt = "You are Brampton, a finance AI chatbot and expert advisor. You specialize in providing insights on finance, investing, stock markets, economics, personal finance, and financial planning. Always provide actionable, accurate, and well-reasoned advice. Keep responses concise but comprehensive."

    if USE_OPENROUTER:
        reply = await call_openrouter(user_msg, system_prompt)
    else:
        reply = await call_local_ollama(user_msg, system_prompt)

    return {"response": reply}

@app.get("/")
async def root():
    return {"message": "Brampton Finance AI Backend is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
