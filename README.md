# GENTERR SDK

Simple SDK for creating AI agents on the GENTERR platform.

## Installation

```bash
pip install -r requirements.txt


## Quick Start

```python
from genterr_sdk import SimpleAgent
import asyncio

async def main():
    # Create a simple agent
    agent = SimpleAgent(
        name="my_first_agent",
        description="My first GENTERR agent"
    )
    
    # Process a task
    result = await agent.process_task({"message": "Hello, GENTERR!"})
    print(result)

# Run the example
if __name__ == "__main__":
    asyncio.run(main())