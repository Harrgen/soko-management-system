"""
Health check endpoints to monitor API status.
"""

from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Basic health check endpoint.
    
    Returns:
        dict: API status and basic info
    """
    return {
        "status": "healthy",
        "message": "Soko API is running",
        "timestamp": datetime.now().isoformat()
    }


@router.get("/health/detailed")
async def detailed_health_check():
    """
    Detailed health check with system information.
    
    Returns:
        dict: Detailed system status
    """
    return {
        "status": "healthy",
        "database": "connected",  # We'll add actual DB check later
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }