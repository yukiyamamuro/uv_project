import asyncio

from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContextConfig
from langchain_openai import ChatOpenAI

browser = Browser(
    config=BrowserConfig(
        disable_security=True,
        headless=False,
        new_context_config=BrowserContextConfig(save_recording_path="./tmp/recordings"),
    )
)
llm = ChatOpenAI(model="gpt-4o")


async def main():
    agents = [
        Agent(task=task, llm=llm, browser=browser)
        for task in [
            "東京の天気を調べてください",
            "Redditのトップストーリーを調べてください",
            "Coinbaseでビットコインの価格を調べてください",
            "NASAの今日の画像を調べてください",
        ]
    ]

    await asyncio.gather(*[agent.run() for agent in agents])

    # async with await browser.new_context() as context:
    agentX = Agent(
        task="Go to apple.com and return the title of the page",
        llm=llm,
        browser=browser,
        # browser_context=context,
    )
    await agentX.run()

    await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
