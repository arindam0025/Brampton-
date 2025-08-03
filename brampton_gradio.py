import gradio as gr
import requests
import json
import os

# Configuration
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY', 'your-api-key-here')

def chat_with_brampton(message, history):
    """
    Main chat function for Brampton Finance AI
    """
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
        # Call OpenRouter API
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

# Create Gradio Interface
def create_brampton_app():
    """
    Create the Gradio chatbot interface
    """
    
    # Custom CSS for modern look
    custom_css = """
    .gradio-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .chat-message {
        border-radius: 15px;
        padding: 10px 15px;
        margin: 5px 0;
    }
    
    .user-message {
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        color: white;
        margin-left: 20%;
    }
    
    .bot-message {
        background: rgba(30, 41, 59, 0.8);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(59, 130, 246, 0.1);
        color: white;
        margin-right: 20%;
    }
    """
    
    # Create the chatbot interface
    with gr.Blocks(
        title="💼 Brampton Finance AI",
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="purple",
            neutral_hue="slate"
        ),
        css=custom_css
    ) as app:
        
        # Header
        gr.HTML("""
        <div style="text-align: center; padding: 20px;">
            <h1 style="background: linear-gradient(135deg, #3b82f6, #8b5cf6, #06b6d4); 
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                       font-size: 2.5em; font-weight: bold; margin: 0;">
                📈 Brampton Finance AI
            </h1>
            <p style="color: #64748b; font-size: 1.1em; margin: 10px 0;">
                Your Expert Finance & Investment Assistant
            </p>
            <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-top: 10px;">
                <div style="width: 8px; height: 8px; background: #10b981; border-radius: 50%; animation: pulse 2s infinite;"></div>
                <span style="color: #10b981; font-size: 0.9em;">AI Online</span>
            </div>
        </div>
        """)
        
        # Chatbot interface
        chatbot = gr.Chatbot(
            value=[["👋", "Hello! I'm Brampton, your finance AI assistant. Ask me anything about investing, markets, economics, or financial planning!"]],
            height=500,
            show_label=False,
            container=True,
            bubble_full_width=False
        )
        
        # Input area
        with gr.Row():
            msg = gr.Textbox(
                placeholder="Ask about stocks, investments, market trends...",
                show_label=False,
                scale=4,
                container=False
            )
            send_btn = gr.Button("💬 Send", scale=1, variant="primary")
        
        # Example questions
        gr.Examples(
            examples=[
                "What's the best investment strategy for beginners?",
                "How should I diversify my portfolio?",
                "What are the current market trends?",
                "Should I invest in cryptocurrency?",
                "How much should I save for retirement?",
                "What are the risks of stock market investing?",
                "Explain compound interest and its benefits",
                "What's the difference between stocks and bonds?"
            ],
            inputs=msg,
            label="💡 Try asking about:"
        )
        
        # Footer
        gr.HTML("""
        <div style="text-align: center; padding: 20px; color: #64748b; font-size: 0.9em;">
            <p>⚠️ <strong>Disclaimer:</strong> This is for educational purposes only. Always consult with a qualified financial advisor before making investment decisions.</p>
            <p>🚀 Powered by OpenRouter API & Llama 3.1</p>
        </div>
        """)
        
        # Handle message sending
        def respond(message, chat_history):
            if not message.strip():
                return "", chat_history
            
            # Add user message to history
            chat_history.append([message, None])
            
            # Get AI response
            bot_response = chat_with_brampton(message, chat_history)
            
            # Add bot response to history
            chat_history[-1][1] = bot_response
            
            return "", chat_history
        
        # Connect the interface
        msg.submit(respond, [msg, chatbot], [msg, chatbot])
        send_btn.click(respond, [msg, chatbot], [msg, chatbot])
    
    return app

if __name__ == "__main__":
    # Create and launch the app
    app = create_brampton_app()
    
    print("🚀 Starting Brampton Finance AI...")
    print("💼 Your finance assistant is ready!")
    
    # Launch the app
    app.launch(
        server_name="0.0.0.0",  # Allow external access
        server_port=7860,       # Default Gradio port
        share=True,             # Create public link
        show_error=True,
        show_tips=True,
        inbrowser=True          # Open in browser automatically
    )
