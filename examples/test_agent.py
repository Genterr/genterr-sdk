from genterr_sdk import SimpleAgent
import asyncio

async def main():
    agent = SimpleAgent("test_agent", "Testing the SDK")
    result = await agent.process_task({"test": "Hello world"})
    print(result)

if __name__ == "__main__":
    asyncio.run(main())