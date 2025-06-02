from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

# Read GOOGLE_API_KEY into env
load_dotenv()

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

async def main():
    agent = Agent(
        task="Go to duckduckgo search and search for 'ducks'. Then navigate to the second link.",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
