"""
GENTERR API Client
=================

Client for interacting with the GENTERR platform API.
"""

import aiohttp
from typing import Dict, Any, Optional
from datetime import datetime, UTC

class GenterrAPI:
    """Client for interacting with the GENTERR platform API."""
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.genterr.com/v1",
        timeout: int = 30
    ):
        """Initialize the GENTERR API client.
        
        Args:
            api_key: API key for authentication
            base_url: Base URL for the GENTERR API
            timeout: Request timeout in seconds
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self._session: Optional[aiohttp.ClientSession] = None
    
    async def __aenter__(self):
        """Create session when entering context."""
        self._session = aiohttp.ClientSession(
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "User-Agent": "GENTERR-SDK/0.1.0"
            }
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Close session when exiting context."""
        if self._session:
            await self._session.close()
            self._session = None
    
    async def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make a request to the GENTERR API.
        
        Args:
            method: HTTP method to use
            endpoint: API endpoint to call
            data: Optional request data
            
        Returns:
            API response data
            
        Raises:
            GenterrAPIError: If the API returns an error
            RuntimeError: If used outside context manager
        """
        if not self._session:
            raise RuntimeError("API client must be used as context manager")
            
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        async with self._session.request(
            method=method,
            url=url,
            json=data,
            timeout=self.timeout
        ) as response:
            response_data = await response.json()
            
            if not 200 <= response.status < 300:
                raise GenterrAPIError(
                    f"API request failed: {response.status} - {response_data.get('message', 'Unknown error')}"
                )
            
            return response_data
    
    async def create_agent(self, agent_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new agent on the GENTERR platform."""
        return await self._request("POST", "/agents", data=agent_data)
    
    async def get_agent(self, agent_id: str) -> Dict[str, Any]:
        """Get agent details by ID."""
        return await self._request("GET", f"/agents/{agent_id}")

class GenterrAPIError(Exception):
    """Exception raised for GENTERR API errors."""
    pass