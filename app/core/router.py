from fastapi import APIRouter
from app.routes import *

api_router = APIRouter(prefix="/api/v1")

# Include sub-routes
def get_api_router() -> APIRouter:
    """
    Returns the configured API router with all routes included.
    This function should be called by the main FastAPI application.
    
    Returns:
        APIRouter: The configured router with all routes included
    """
    return api_router
