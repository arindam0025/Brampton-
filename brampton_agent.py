from utils.llm_client import ask_gpt, ask_claude

def run_brampton(query):
    gpt_response = ask_gpt(query)
    claude_response = ask_claude(query)

    return {
        "ChatGPT": gpt_response,
        "Claude": claude_response
    }
