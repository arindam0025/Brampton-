# Brampton AI - Finance Assistant Chatbot

🤖 **Brampton AI** is an intelligent finance assistant powered by both GPT-4 and Claude, providing comprehensive financial guidance with a beautiful modern web interface.

## Features

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

### Local Development

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
