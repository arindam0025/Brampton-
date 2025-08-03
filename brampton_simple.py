import gradio as gr
import requests

# Configuration
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY', 'your-api-key-here')

def chat_with_brampton(message, history):
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
            return f"❌ API Error: {response.status_code}"
            
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Create simple Gradio interface
with gr.Blocks(title="💼 Brampton Finance AI") as app:
    
    gr.HTML("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #1e293b, #0f172a); border-radius: 10px; margin-bottom: 20px;">
        <h1 style="color: #3b82f6; font-size: 2.5em; margin: 0;">📈 Brampton Finance AI</h1>
        <p style="color: #64748b; font-size: 1.1em;">Your Expert Finance & Investment Assistant</p>
        <div style="color: #10b981;">🟢 AI Online</div>
    </div>
    """)
    
    chatbot = gr.Chatbot(
        value=[["👋", "Hello! I'm Brampton, your finance AI assistant. Ask me anything about investing, markets, economics, or financial planning!"]],
        height=400
    )
    
    msg = gr.Textbox(
        placeholder="Ask about stocks, investments, market trends...",
        label="Your Question"
    )
    
    send_btn = gr.Button("💬 Send", variant="primary")
    
    gr.Examples(
        examples=[
            "What's the best investment strategy for beginners?",
            "How should I diversify my portfolio?",
            "What are the current market trends?",
            "Should I invest in cryptocurrency?",
            "How much should I save for retirement?"
        ],
        inputs=msg
    )
    
    gr.HTML("""
    <div style="text-align: center; padding: 10px; color: #64748b; font-size: 0.9em;">
        <p>⚠️ Disclaimer: For educational purposes only. Consult a qualified financial advisor before making investment decisions.</p>
    </div>
    """)
    
    def respond(message, chat_history):
        if not message.strip():
            return "", chat_history
        
        chat_history.append([message, None])
        bot_response = chat_with_brampton(message, chat_history)
        chat_history[-1][1] = bot_response
        return "", chat_history
    
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    send_btn.click(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    print("🚀 Starting Brampton Finance AI...")
    print("💼 Your finance assistant is ready!")
    
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,
        inbrowser=True
    )
