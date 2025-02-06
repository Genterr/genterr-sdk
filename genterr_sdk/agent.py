from typing import Dict, Any
from datetime import datetime
import logging
import asyncio
from uuid import uuid4, UUID

class SimpleAgent:
    """
    Basic agent class for GENTERR platform
    """
    def __init__(self, name: str, description: str = ""):
        self.agent_id: UUID = uuid4()
        self.name = name
        self.description = description
        self.created_at = datetime.utcnow()
        self.status = "initialized"
        self.metrics = {
            "tasks_completed": 0,
            "success_rate": 0.0,
            "errors": 0
        }
        
        # Setup logging
        self.logger = logging.getLogger(f"genterr.{name}")
        self._setup_logging()
    
    def _setup_logging(self):
        """Setup basic logging configuration"""
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)
    
    async def process_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a task - override this method in your agent
        """
        self.logger.info(f"Processing task: {task}")
        try:
            # Simulate some processing time
            await asyncio.sleep(1)
            self.metrics["tasks_completed"] += 1
            return {
                "status": "completed",
                "result": "Task processed successfully",
                "agent_id": str(self.agent_id)
            }
        except Exception as e:
            self.logger.error(f"Error processing task: {str(e)}")
            self.metrics["errors"] += 1
            raise