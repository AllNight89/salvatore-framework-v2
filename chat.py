import asyncio
from main import SalvatoreAgent

def chat():
    agent = SalvatoreAgent()
    print("Salvatore Truth-Seeker ready—ask away!")
    while True:
        query = input("Claim to check: ")
        if query.lower() == "quit": break
        result = asyncio.run(agent.run(query))
        print(result)

if __name__ == "__main__":
    chat()
