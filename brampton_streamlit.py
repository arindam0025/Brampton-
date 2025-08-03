import streamlit as st
import requests
import json

# Page configuration
st.set_page_config(
    page_title="💼 Brampton Finance AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Configuration
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY', 'your-api-key-here')

# Custom CSS for modern look
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        display: flex;
        align-items: flex-start;
        gap: 0.5rem;
    }
    
    .user-message {
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        color: white;
        margin-left: 20%;
        flex-direction: row-reverse;
    }
    
    .bot-message {
        background: rgba(30, 41, 59, 0.8);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(59, 130, 246, 0.1);
        color: white;
        margin-right: 20%;
    }
    
    .stTextInput > div > div > input {
        background: rgba(30, 41, 59, 0.8);
        color: white;
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 15px;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
    }
</style>
""", unsafe_allow_html=True)

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
        with st.spinner("🤔 Brampton is thinking..."):
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

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hello! I'm Brampton, your finance AI assistant. Ask me anything about investing, markets, economics, or financial planning!"}
    ]

# Header
st.markdown("""
<div style="text-align: center; padding: 20px; background: rgba(30, 41, 59, 0.8); backdrop-filter: blur(20px); border: 1px solid rgba(59, 130, 246, 0.1); border-radius: 15px; margin-bottom: 20px;">
    <h1 style="background: linear-gradient(135deg, #3b82f6, #8b5cf6, #06b6d4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5em; margin: 0;">
        📈 Brampton Finance AI
    </h1>
    <p style="color: #64748b; font-size: 1.1em; margin: 10px 0;">
        Your Expert Finance & Investment Assistant
    </p>
    <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-top: 10px;">
        <div style="width: 8px; height: 8px; background: #10b981; border-radius: 50%;"></div>
        <span style="color: #10b981; font-size: 0.9em;">🤖 AI Online</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"""
        <div class="chat-message user-message">
            <div>
                <div style="font-weight: bold; margin-bottom: 5px;">👤 You</div>
                <div>{message["content"]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message bot-message">
            <div>
                <div style="font-weight: bold; margin-bottom: 5px;">🤖 Brampton</div>
                <div>{message["content"]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Chat input
col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input(
        "Ask about stocks, investments, market trends...",
        key="user_input",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("💬 Send", use_container_width=True)

# Handle user input
if send_button and user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get AI response
    ai_response = chat_with_brampton(user_input)
    
    # Add AI response
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    
    # Rerun to update the chat
    st.rerun()

# Example questions
st.markdown("### 💡 Try asking about:")
col1, col2 = st.columns(2)

with col1:
    if st.button("What's the best investment strategy for beginners?"):
        st.session_state.messages.append({"role": "user", "content": "What's the best investment strategy for beginners?"})
        ai_response = chat_with_brampton("What's the best investment strategy for beginners?")
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.rerun()
    
    if st.button("How should I diversify my portfolio?"):
        st.session_state.messages.append({"role": "user", "content": "How should I diversify my portfolio?"})
        ai_response = chat_with_brampton("How should I diversify my portfolio?")
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.rerun()

with col2:
    if st.button("What are the current market trends?"):
        st.session_state.messages.append({"role": "user", "content": "What are the current market trends?"})
        ai_response = chat_with_brampton("What are the current market trends?")
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.rerun()
    
    if st.button("Should I invest in cryptocurrency?"):
        st.session_state.messages.append({"role": "user", "content": "Should I invest in cryptocurrency?"})
        ai_response = chat_with_brampton("Should I invest in cryptocurrency?")
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.rerun()

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hello! I'm Brampton, your finance AI assistant. Ask me anything about investing, markets, economics, or financial planning!"}
    ]
    st.rerun()

# Footer
st.markdown("""
<div style="text-align: center; padding: 20px; color: #64748b; font-size: 0.9em; margin-top: 30px;">
    <p>⚠️ <strong>Disclaimer:</strong> This is for educational purposes only. Always consult with a qualified financial advisor before making investment decisions.</p>
    <p>🚀 Powered by OpenRouter API & Llama 3.1</p>
</div>
""", unsafe_allow_html=True)
