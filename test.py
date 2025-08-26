import asyncio
from salvatore import SAL

async def main():
    sal = SAL("JuggernautApex")
    result = await sal.run("Analyze X post")
    print(result)

asyncio.run(main())
