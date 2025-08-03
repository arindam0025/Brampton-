#!/usr/bin/env python3
"""
Simple launcher for Brampton AI - No installation required!
"""

import sys
import os
import subprocess
import webbrowser
import time
import threading
import tempfile

def install_requirements():
    """Install required packages if not already installed"""
    required_packages = [
        'flask>=2.3.3',
        'openai>=1.3.0', 
        'anthropic>=0.25.0',
        'python-dotenv>=1.0.0',
        'requests>=2.31.0'
    ]
    
    print("📦 Checking and installing required packages...")
    for package in required_packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            print(f"⚠️  Could not install {package}, continuing...")

def create_env_file():
    """Create .env file with demo keys"""
    if not os.path.exists('.env'):
        env_content = """# Brampton AI Environment Variables
# Using demo mode - no real API keys needed!

OPENAI_API_KEY=demo-key-for-brampton-ai
ANTHROPIC_API_KEY=demo-key-for-brampton-ai
"""
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ Created .env file with demo mode")

def create_html_template():
    """Create the HTML template"""
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brampton AI - Finance Assistant</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            padding: 40px;
            max-width: 800px;
            width: 100%;
            text-align: center;
        }
        
        .header {
            margin-bottom: 30px;
        }
        
        .header h1 {
            color: #333;
            font-size: 2.5em;
            margin-bottom: 10px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .header p {
            color: #666;
            font-size: 1.1em;
        }
        
        .chat-form {
            margin-bottom: 30px;
        }
        
        .input-group {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        input[type="text"] {
            flex: 1;
            padding: 15px 20px;
            border: 2px solid #e1e5e9;
            border-radius: 10px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        input[type="text"]:focus {
            outline: none;
            border-color: #667eea;
        }
        
        button {
            padding: 15px 30px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        button:hover {
            transform: translateY(-2px);
        }
        
        .responses {
            text-align: left;
        }
        
        .response {
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 15px;
            border-left: 4px solid #667eea;
        }
        
        .response h3 {
            color: #333;
            margin-bottom: 10px;
            font-size: 1.2em;
        }
        
        .response p {
            color: #555;
            line-height: 1.6;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        
        .feature {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
        }
        
        .feature h3 {
            margin-bottom: 10px;
        }
        
        .welcome {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 30px;
        }
        
        .welcome h2 {
            margin-bottom: 15px;
        }
        
        .welcome p {
            opacity: 0.9;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 Brampton AI</h1>
            <p>Advanced Finance Assistant</p>
        </div>
        
        <div class="welcome">
            <h2>Welcome to Brampton AI!</h2>
            <p>Ask me anything about finance, investments, market analysis, or corporate finance. I'm here to help you make informed financial decisions.</p>
        </div>
        
        <form method="POST" class="chat-form">
            <div class="input-group">
                <input type="text" name="query" placeholder="Ask me about finance, investments, or market analysis..." required>
                <button type="submit">Ask Brampton</button>
            </div>
        </form>
        
        {% if query %}
        <div class="responses">
            <h3>Your Question: "{{ query }}"</h3>
            {% if answers %}
                {% for ai, response in answers.items() %}
                <div class="response">
                    <h3>{{ ai }}</h3>
                    <p>{{ response }}</p>
                </div>
                {% endfor %}
            {% endif %}
        </div>
        {% endif %}
        
        <div class="features">
            <div class="feature">
                <h3>📊 Investment Analysis</h3>
                <p>Get detailed investment insights and recommendations</p>
            </div>
            <div class="feature">
                <h3>💰 Financial Planning</h3>
                <p>Personalized financial planning strategies</p>
            </div>
            <div class="feature">
                <h3>🛡️ Risk Management</h3>
                <p>Comprehensive risk assessment and mitigation</p>
            </div>
            <div class="feature">
                <h3>🏢 Corporate Finance</h3>
                <p>Expert corporate finance guidance</p>
            </div>
        </div>
    </div>
</body>
</html>
"""
    
    # Create temporary directory for templates
    temp_dir = tempfile.mkdtemp()
    template_dir = os.path.join(temp_dir, 'templates')
    os.makedirs(template_dir, exist_ok=True)
    
    # Write HTML template
    template_path = os.path.join(template_dir, 'index.html')
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return temp_dir

def start_server():
    """Start the Flask server"""
    try:
        # Import Flask and create app
        from flask import Flask, render_template, request
        import os
        from dotenv import load_dotenv
        
        load_dotenv()
        
        # Create template directory
        temp_dir = create_html_template()
        
        app = Flask(__name__, template_folder=os.path.join(temp_dir, 'templates'))
        
        # Simple chat function
        def get_ai_response(query):
            return {
                "ChatGPT": f"🤖 ChatGPT: I'm here to help with your finance question: '{query}'. This is a demo response showing how Brampton AI works. In a full implementation, I would provide detailed financial analysis and recommendations.",
                "Claude": f"🧠 Claude: Great question about '{query}'! Here's my analysis for you. I would typically provide comprehensive financial insights, market analysis, and actionable recommendations based on your specific query."
            }
        
        @app.route('/', methods=['GET', 'POST'])
        def home():
            if request.method == 'POST':
                user_query = request.form['query']
                answers = get_ai_response(user_query)
                return render_template('index.html', query=user_query, answers=answers)
            return render_template('index.html')
        
        # Start server
        port = 5000
        host = '127.0.0.1'
        
        print(f"🚀 Starting Brampton AI server...")
        print(f"🌐 Server will be available at: http://{host}:{port}")
        
        # Start server in background
        def run_server():
            app.run(host=host, port=port, debug=False, use_reloader=False)
        
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        
        # Wait for server to start
        time.sleep(3)
        
        # Open browser
        url = f"http://{host}:{port}"
        print(f"🌐 Opening Brampton AI in your browser...")
        try:
            webbrowser.open(url)
        except:
            print(f"🌐 Please open your browser and go to: {url}")
        
        print("\n🤖 Brampton AI is ready!")
        print("💡 Ask me anything about finance, investments, or market analysis")
        print("🛑 Press Ctrl+C to stop the server")
        
        # Keep running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n👋 Shutting down Brampton AI...")
            sys.exit(0)
            
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

def main():
    """Main function"""
    print("🤖 Brampton AI - Finance Assistant")
    print("=" * 40)
    
    # Install requirements
    install_requirements()
    
    # Create .env file
    create_env_file()
    
    # Start server
    start_server()

if __name__ == "__main__":
    main() 