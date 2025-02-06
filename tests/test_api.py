import pytest
import aiohttp
from unittest.mock import AsyncMock, MagicMock
from genterr_sdk.api import GenterrAPI, GenterrAPIError
from types import SimpleNamespace

class MockResponse:
    """Mock class for HTTP responses in tests"""
    def __init__(self, status: int, data: dict):
        self.status = status
        self._data = data

    async def json(self):
        return self._data

class RequestContextManager:
    """Async context manager for request responses"""
    def __init__(self, response: MockResponse):
        self.response = response

    async def __aenter__(self):
        return self.response

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

class MockClientSession:
    """Mock class for aiohttp.ClientSession"""
    def __init__(self, response: MockResponse):
        self.response = response
        self.request = self._make_request
        self.close = AsyncMock()

    def _make_request(self, *args, **kwargs):
        return RequestContextManager(self.response)

@pytest.mark.asyncio
async def test_create_agent():
    """Test creating a new agent"""
    response = MockResponse(
        status=200,
        data={"id": "test-agent-id", "name": "Test Agent"}
    )
    
    async with GenterrAPI("test-api-key") as client:
        client._session = MockClientSession(response)
        
        result = await client.create_agent({
            "name": "Test Agent",
            "description": "Test Description"
        })
        
        assert result["id"] == "test-agent-id"
        assert result["name"] == "Test Agent"

@pytest.mark.asyncio
async def test_api_error():
    """Test API error handling"""
    response = MockResponse(
        status=400,
        data={"message": "Invalid request"}
    )
    
    async with GenterrAPI("test-api-key") as client:
        client._session = MockClientSession(response)
        
        with pytest.raises(GenterrAPIError) as exc_info:
            await client.create_agent({
                "invalid": "data"
            })
        
        assert "API request failed: 400" in str(exc_info.value)

@pytest.mark.asyncio
async def test_get_agent():
    """Test getting agent details"""
    response = MockResponse(
        status=200,
        data={
            "id": "test-agent-id",
            "name": "Test Agent",
            "status": "active"
        }
    )
    
    async with GenterrAPI("test-api-key") as client:
        client._session = MockClientSession(response)
        
        result = await client.get_agent("test-agent-id")
        
        assert result["id"] == "test-agent-id"
        assert result["status"] == "active"

@pytest.mark.asyncio
async def test_session_cleanup():
    """Test session cleanup on context exit"""
    client = GenterrAPI("test-api-key")
    assert client._session is None
    
    async with client as session:
        assert session._session is not None
        session._session = MockClientSession(MockResponse(200, {}))
    
    assert session._session is None