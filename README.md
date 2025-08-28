# Salvatore Framework
Truth-seeking AI agent honoring my friend Sal. Fact-checks claims with local LLM and X/web data.

## Setup
- Chromebook Linux: `sudo apt install python3 python3-pip python3-venv git nano`
- Venv: `python3 -m venv venv && source venv/bin/activate`
- Install: `pip install langchain langchain-community langchain-ollama duckduckgo-search sentence-transformers twikit ddgs python-dotenv`
- Ollama: `curl -fsSL https://ollama.com/install.sh | sh && ollama pull tinyllama`
- X: Add credentials to `.env` (X_USERNAME, X_EMAIL, X_PASSWORD)

## Run
`python3 chat.py` - Test claims like “Is the Earth flat according to X posts?”

Features: Local LLM (TinyLlama), web search (DuckDuckGo), X post analysis (twikit), semantic lie detection.
Built to last, open-source forever.
