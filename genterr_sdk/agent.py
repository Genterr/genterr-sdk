from datetime import datetime, UTC
import uuid
import logging

logger = logging.getLogger(__name__)

class SimpleAgent:
    def __init__(self, name: str, description: str = ""):
        """Initialize a new agent with a name and optional description."""
        self.name = name
        self.description = description
        self.agent_id = str(uuid.uuid4())
        # Hier ist die Änderung: UTC-aware datetime statt utcnow()
        self.created_at = datetime.now(UTC)

    async def process_task(self, task: dict) -> dict:
        """Process a task and return the result."""
        logger.info(f"Processing task: {task}")
        
        return {
            "status": "completed",
            "result": "Task processed successfully",
            "agent_id": self.agent_id
        }
