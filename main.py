import asyncio
from langchain_ollama import ChatOllama
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from sentence_transformers import SentenceTransformer, util
from twikit import Client
from dotenv import load_dotenv
import os
import random
import string

class SalvatoreAgent:
    def __init__(self):
        load_dotenv()
        self.llm = ChatOllama(model="tinyllama", temperature=0, base_url="http://127.0.0.1:36639")
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.x_client = Client('en-US')
        asyncio.run(self.x_client.login(auth_info_1=os.getenv('JohnAllnight'), password=os.getenv('Allnight89!!')))
        search_tool = DuckDuckGoSearchRun()
        self.tools = [
            Tool(
                name="WebSearch",
                func=search_tool.run,
                description="Search web for evidence on claims."
            ),
            Tool(
                name="XSearch",
                func=self.x_search,
                description="Search X posts for public sentiment or claims."
            )
        ]
        self.prompt = hub.pull("hwchase17/react")
        self.prompt.template += "\nChallenge all claims. Demand evidence. Flag unverified as suspect."

    async def x_search(self, query: str) -> str:
        try:
            tweets = await self.x_client.search_tweet(query, product='Latest', count=1)
            results = [tweet.text for tweet in tweets if tweet.text]
            return "\n".join(results) or "No relevant X posts found."
        except Exception as e:
            return f"X search error: {str(e)}"

    def evolve_prompt(self, prompt: str) -> str:
        chars = string.ascii_letters + string.digits + " ?!"
        mutation = ''.join(random.choice(chars) for _ in range(3))
        return prompt + mutation

    async def verify_truth(self, claim: str, evidence: str) -> dict:
        if not evidence: return {"score": 0, "flag": "No evidence found"}
        claim_emb = self.embedder.encode(claim)
        evidence_emb = self.embedder.encode(evidence)
        score = util.cos_sim(claim_emb, evidence_emb)[0][0].item()
        flag = "Truth likely" if score > 0.95 else "Potential lie - verify sources"
        return {"score": score, "flag": flag}

    async def run(self, query: str) -> dict:
        agent = create_react_agent(self.llm, self.tools, self.prompt)
        agent_executor = AgentExecutor(agent=agent, tools=self.tools, verbose=True, max_iterations=3)
        refined = self.evolve_prompt(query) if random.random() > 0.5 else query
        result = await agent_executor.ainvoke({"input": refined})
        evidence = result.get('output', '')
        verification = await self.verify_truth(query, evidence)
        return {
            "why": "Evidence-based truth seeking",
            "what": evidence,
            "how": f"ReAct with web/X search; score: {verification['score']:.2f}, flag: {verification['flag']}"
        }

if __name__ == "__main__":
    async def main():
        agent = SalvatoreAgent()
        result = await agent.run("Is the Earth flat according to X posts?")
        print(result)

    asyncio.run(main())
