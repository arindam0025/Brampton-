# Brampton Finance AI Chatbot

**Brampton** is a finance-focused AI chatbot powered by **Ollama 3.1** with a beautiful ChatGPT-like interface. Get expert insights on investing, markets, economics, and financial planning!

## Features

- **Local AI Model** using Ollama 3.1 (Llama 3)
- **OpenRouter API** support with your provided API key
- **Finance Expert** persona for investment and market insights
- **Modern UI** inspired by ChatGPT/Lovable with React + Tailwind
- **FastAPI Backend** for high-performance API responses
- **Easy Setup** with automated scripts
- 🧠 **Dual AI Power**: Combines responses from both GPT-4 and Claude
- 💰 **Finance Focused**: Specialized in corporate finance, investment analysis, and risk modeling
- 🎨 **Modern Interface**: Beautiful, responsive web design
- 🚀 **Easy Deployment**: Ready for local use or cloud deployment

## Screenshot

The interface features a clean, modern design with:
- Animated welcome screen with feature cards
- Real-time chat interface
- Distinct avatars for different AI models
- Professional finance-focused styling

## Quick Start

### Option 1: One-Click Installation (Recommended)

#### Windows Users:
1. **Download and run the installer**
   ```cmd
   git clone https://github.com/arindam0025/Brampton-.git
   cd Brampton-
   install.bat
   ```

#### Mac/Linux Users:
1. **Download and run the installer**
   ```bash
   git clone https://github.com/arindam0025/Brampton-.git
   cd Brampton-
   chmod +x install.sh
   ./install.sh
   ```

### Option 2: Manual Installation

1. **Install from PyPI** (when available)
   ```bash
   pip install brampton-ai
   ```

2. **Or install from source**
   ```bash
   git clone https://github.com/arindam0025/Brampton-.git
   cd Brampton-
   pip install -e .
   ```

3. **Set up API keys interactively**
   ```bash
   brampton-ai --setup
   ```
   This will prompt you to enter your API keys and automatically create the `.env` file.

4. **Run the application**
   ```bash
   brampton-ai
   ```
   
   **If "brampton-ai" command is not found, try these alternatives:**
   ```bash
   # Method 1: Use the batch file (Windows)
   run.bat
   
   # Method 2: Use the Python launcher
   python start_brampton.py
   
   # Method 3: Direct module execution
   python -m brampton_ai.cli
   ```

5. **Access the web interface**
   The application will automatically open in your browser at `http://127.0.0.1:5000`

### CLI Options

The `brampton-ai` command supports several options:

```bash
# Interactive setup for API keys
brampton-ai --setup

# Start on a different port
brampton-ai --port 8080

# Start on a specific host
brampton-ai --host 0.0.0.0

# Start without opening browser automatically
brampton-ai --no-browser

# Run in debug mode
brampton-ai --debug

# Get help
brampton-ai --help
```

### Option 3: Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/arindam0025/Brampton-.git
   cd Brampton-
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

### Deploy to Render

1. **Push to GitHub** (already done)

2. **Go to [Render.com](https://render.com)**

3. **Create a new Web Service**
   - Connect your GitHub repository
   - Use these settings:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn main:app`

4. **Add Environment Variables**
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `ANTHROPIC_API_KEY`: Your Anthropic API key

5. **Deploy!** 🚀

## Project Structure

```
brampton-chatbot/
│
├── main.py                 # Flask application entry point
├── brampton_agent.py       # Core chatbot logic
├── utils/
│   └── llm_client.py       # API client for GPT-4 and Claude
├── templates/
│   └── index.html          # Beautiful web interface
├── static/
│   └── styles.css          # Modern CSS styling
├── prompts/
│   └── brampton_prompt.txt # AI personality configuration
├── .env                    # Environment variables (not in repo)
├── requirements.txt        # Python dependencies
├── Procfile               # Deployment configuration
└── README.md              # This file

```

## Usage

Ask Brampton about:
- 📊 Investment Analysis
- 💰 Financial Planning  
- 🛡️ Risk Management
- 🏢 Corporate Finance
- 📈 Market Analysis
- 💡 Financial Strategy

## API Keys Required

- **OpenAI API Key**: For GPT-4 access
- **Anthropic API Key**: For Claude access

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **AI Models**: GPT-4, Claude-3-Haiku
- **Deployment**: Render, Gunicorn
- **Styling**: Modern CSS with gradients and animations

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Brampton AI** - Your Advanced Finance Assistant 🤖💰 