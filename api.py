from fastapi import FastAPI
from pydantic import BaseModel
from salvatore import SAL
import asyncio

app = FastAPI()

class ChatRequest(BaseModel):
    query: str
    tier: str = "Light"
    choice: str = "default"

@app.post("/chat")
async def chat(request: ChatRequest):
    sal = SAL(request.tier)
    result = await sal.run(request.query, request.choice)
    return {"reply": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
