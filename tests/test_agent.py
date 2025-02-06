import pytest
import asyncio
from genterr_sdk import SimpleAgent

@pytest.mark.asyncio
async def test_simple_agent_creation():
    """Test SimpleAgent initialization."""
    agent = SimpleAgent(
        name="test_agent",
        description="Test agent description"
    )
    assert agent.name == "test_agent"
    assert agent.description == "Test agent description"
    assert agent.metrics["tasks_completed"] == 0
    assert agent.metrics["success_rate"] == 0.0
    assert agent.metrics["rating"] == 0.0

@pytest.mark.asyncio
async def test_process_task():
    """Test task processing."""
    agent = SimpleAgent(
        name="test_agent",
        description="Test agent description"
    )
    task = {"message": "Hello, Test!"}
    result = await agent.process_task(task)
    
    assert result["status"] == "completed"
    assert "Hello, Test!" in result["result"]
    assert result["agent_name"] == "test_agent"
    assert result["metrics"]["tasks_completed"] == 1

@pytest.mark.asyncio
async def test_metrics_update():
    """Test metrics updating."""
    agent = SimpleAgent(
        name="test_agent",
        description="Test agent description"
    )
    
    # Process a task and update metrics
    await agent.process_task({"message": "Test"})
    agent.update_metrics(success=True, rating=4.5)
    
    assert agent.metrics["tasks_completed"] == 1
    assert agent.metrics["success_rate"] == 1.0
    assert agent.metrics["rating"] == 4.5

@pytest.mark.asyncio
async def test_agent_training():
    """Test agent training functionality."""
    agent = SimpleAgent(
        name="test_agent",
        description="Test agent description"
    )
    
    training_data = {
        "examples": [
            {"input": "Hello", "output": "Hi there!"}
        ]
    }
    
    result = await agent.train(training_data)
    assert result["status"] == "training_completed"
    assert "metrics" in result