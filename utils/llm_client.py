import os
from openai import OpenAI
import anthropic
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize Anthropic client
claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def ask_gpt(prompt):
    """Get response from GPT-4"""
    try:
        # Add finance context to the prompt
        finance_prompt = f"You are Brampton, a smart and friendly AI trained in corporate finance, investment analysis, and risk modeling. Answer like a helpful analyst, not a professor.\n\nUser question: {prompt}"
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": finance_prompt}],
            temperature=0.7,
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry, I'm having trouble connecting to GPT-4 right now. Error: {str(e)}"

def ask_claude(prompt):
    """Get response from Claude"""
    try:
        # Add finance context to the prompt
        finance_prompt = f"You are Brampton, a smart and friendly AI trained in corporate finance, investment analysis, and risk modeling. Answer like a helpful analyst, not a professor.\n\nUser question: {prompt}"
        
        response = claude.messages.create(
            model="claude-3-haiku-20240307",  # Using Haiku as it's more cost-effective
            max_tokens=800,
            messages=[{"role": "user", "content": finance_prompt}]
        )
        return response.content[0].text
    except Exception as e:
        return f"Sorry, I'm having trouble connecting to Claude right now. Error: {str(e)}"
