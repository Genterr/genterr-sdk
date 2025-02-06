"""
GENTERR SDK
===========

A Python SDK for creating and managing AI agents on the GENTERR platform.
"""

from .agent import SimpleAgent
from .config import Config

__version__ = "0.1.0"
__all__ = ["SimpleAgent", "Config"]