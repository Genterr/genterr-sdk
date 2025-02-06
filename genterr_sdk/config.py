from typing import Dict, Any

class Config:
    """Configuration for GENTERR SDK."""
    
    # API endpoints
    API_BASE_URL = "https://api.genterr.com/v1"
    
    # Default agent settings
    DEFAULT_AGENT_SETTINGS = {
        "max_tokens": 1000,
        "temperature": 0.7,
        "top_p": 0.9,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }
    
    # Supported agent capabilities
    SUPPORTED_CAPABILITIES = [
        "text_processing",
        "code_generation",
        "data_analysis",
        "content_creation",
        "trading",
        "research"
    ]
    
    @staticmethod
    def validate_agent_settings(settings: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate and merge agent settings with defaults.
        
        Args:
            settings: Custom agent settings
            
        Returns:
            Merged settings dictionary
        """
        validated = DEFAULT_AGENT_SETTINGS.copy()
        validated.update(settings)
        return validated