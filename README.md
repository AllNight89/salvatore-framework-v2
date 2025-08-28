# Salvatore Framework
Truth-seeking AI agent honoring my friend Sal. Fact-checks claims with local LLM.

## Setup
- Chromebook Linux: `sudo apt install python3 python3-pip python3-venv git nano`
- Venv: `python3 -m venv venv && source venv/bin/activate`
- Install: `pip install langchain langchain-community langchain-ollama duckduckgo-search sentence-transformers`
- Ollama: `curl -fsSL https://ollama.com/install.sh | sh && ollama pull phi3:mini`

## Run
`python3 chat.py` - Test claims like “Moon landing was fake.”

Built to last, open-source forever.
