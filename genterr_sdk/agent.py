from typing import Dict, Any, Optional
import asyncio

class SimpleAgent:
    """Base class for GENTERR agents."""
    
    def __init__(
        self,
        name: str,
        description: str,
        capabilities: Optional[Dict[str, Any]] = None
    ):
        self.name = name
        self.description = description
        self.capabilities = capabilities or {}
        self.metrics = {
            "tasks_completed": 0,
            "success_rate": 0.0,
            "rating": 0.0
        }
    
    async def process_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a task and return the result.
        
        Args:
            task: Dictionary containing task details and data
                 Example: {"message": "Hello, GENTERR!", "type": "text"}
        
        Returns:
            Dictionary containing the task result and metadata
        """
        # Increment tasks completed
        self.metrics["tasks_completed"] += 1
        
        # Basic task processing (to be overridden by specific agent implementations)
        return {
            "status": "completed",
            "result": f"Processed task: {task.get('message', '')}",
            "agent_name": self.name,
            "metrics": self.metrics
        }

    async def train(self, training_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Train the agent with custom data.
        
        Args:
            training_data: Dictionary containing training data and parameters
        
        Returns:
            Dictionary containing training results and metrics
        """
        return {
            "status": "training_completed",
            "metrics": self.metrics
        }

    def update_metrics(self, success: bool, rating: float) -> None:
        """
        Update agent performance metrics.
        
        Args:
            success: Whether the task was completed successfully
            rating: Rating received for the task (1-5)
        """
        total_tasks = self.metrics["tasks_completed"]
        if total_tasks > 0:
            current_success = self.metrics["success_rate"] * (total_tasks - 1)
            self.metrics["success_rate"] = (current_success + int(success)) / total_tasks
            
        current_rating = self.metrics["rating"]
        self.metrics["rating"] = (current_rating + rating) / 2 if current_rating > 0 else rating