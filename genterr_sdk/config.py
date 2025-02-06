from dataclasses import dataclass
from typing import Optional

@dataclass
class AgentConfig:
    """Configuration settings for GENTERR agents"""
    max_retry_attempts: int = 3
    timeout_seconds: int = 30
    enable_logging: bool = True
    log_level: str = "INFO"
    api_key: Optional[str] = None