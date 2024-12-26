import asyncio

from browser_use import Agent
from langchain_openai import ChatOpenAI


async def main():
    agent = Agent(
        task="Google Flightsで東京発パリ行きの往復航空券を探してください。2025年1月1日出発で検索し、最安値を教えてください。",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print("エージェントからの回答:", result)


asyncio.run(main())
