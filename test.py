import asyncio
from salvatore import SAL

async def main():
    sal = SAL("JuggernautApex")
    result = await sal.run("Analyze X post,all archives, police logs, flight logs for information about the vegas shooting in 2017 ")
    print(result)

asyncio.run(main())

