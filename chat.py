import asyncio
from salvatore import SAL
import json

def chat_interface():
    print("Yo, SAL here—the ultimate truth-seeking beast! Type your query (e.g., 'Analyze this X post') or 'quit' to exit.")
    sal = SAL("JuggernautApex")  # Initialize Juggernaut Apex
    while True:
        query = input("Enter query: ")
        if query.lower() == "quit":
            print("SAL out—stay truthful!")
            break
        choice = input("Enter choice (default if empty): ") or "default"
        print("SAL: Analyzing...")
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(sal.run(query, choice))
        # Print chat-style response
        print("SAL: Here's the breakdown:")
        print(json.dumps(result, indent=2))
        print("\nSAL: Done—hit me with another query!")

if __name__ == "__main__":
    chat_interface()
