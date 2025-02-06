import pytest
from genterr_sdk import SimpleAgent

@pytest.mark.asyncio
async def test_simple_agent_creation():
    agent = SimpleAgent(
        name="test_agent",
        description="Test agent description"
    )
    assert agent.name == "test_agent"
    assert agent.description == "Test agent description"

@pytest.mark.asyncio
async def test_process_task():
    agent = SimpleAgent("test_agent", "Test agent")
    result = await agent.process_task({"test": "Hello world"})
    assert isinstance(result, dict)
    assert "status" in result
    assert "result" in result
    assert "agent_id" in result
