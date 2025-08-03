import os
import requests
from dotenv import load_dotenv

load_dotenv()

def ask_gpt(prompt):
    """Get response from GPT-4"""
    try:
        # Add finance context to the prompt
        finance_prompt = f"You are Brampton, a smart and friendly AI trained in corporate finance, investment analysis, and risk modeling. Answer like a helpful analyst, not a professor.\n\nUser question: {prompt}"
        
        headers = {
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "gpt-4",
            "messages": [{"role": "user", "content": finance_prompt}],
            "temperature": 0.7,
            "max_tokens": 800
        }
        
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data
        )
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"GPT-4 Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Sorry, I'm having trouble connecting to GPT-4 right now. Error: {str(e)}"

def ask_claude(prompt):
    """Get response from Claude"""
    try:
        # Add finance context to the prompt
        finance_prompt = f"You are Brampton, a smart and friendly AI trained in corporate finance, investment analysis, and risk modeling. Answer like a helpful analyst, not a professor.\n\nUser question: {prompt}"
        
        headers = {
            "x-api-key": os.getenv("ANTHROPIC_API_KEY"),
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        }
        
        data = {
            "model": "claude-3-haiku-20240307",
            "max_tokens": 800,
            "messages": [{"role": "user", "content": finance_prompt}]
        }
        
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=data
        )
        
        if response.status_code == 200:
            return response.json()["content"][0]["text"]
        else:
            return f"Claude Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Sorry, I'm having trouble connecting to Claude right now. Error: {str(e)}"
