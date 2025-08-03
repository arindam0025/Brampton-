from flask import Flask, render_template, request, jsonify
import requests
import json
import os

app = Flask(__name__)

# Configuration - Use environment variable for security
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY', 'your-api-key-here')

def chat_with_brampton(message):
    """Chat function for Brampton Finance AI"""
    
    system_prompt = """You are Brampton, a finance AI chatbot and expert advisor. You specialize in:
    - Stock market analysis and investment strategies
    - Personal finance and budgeting advice
    - Economic trends and market insights
    - Cryptocurrency and alternative investments
    - Retirement planning and wealth management
    - Risk assessment and portfolio optimization
    
    Always provide actionable, accurate, and well-reasoned advice. 
    Keep responses concise but comprehensive.
    Include relevant disclaimers when giving investment advice."""

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
                    {"role": "user", "content": message}
                ]
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            return f"❌ API Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"❌ Error: {str(e)}"

@app.route('/')
def home():
    """Main page"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Chat API endpoint"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message.strip():
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get AI response
        ai_response = chat_with_brampton(user_message)
        
        return jsonify({
            'response': ai_response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'Brampton Finance AI'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
