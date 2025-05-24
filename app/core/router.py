from fastapi import APIRouter
from app.product.routes import router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(router)

def get_api_router() -> APIRouter:
    """
    Returns the configured API router with all routes included.
    This function should be called by the main FastAPI application.
    
    Returns:
        APIRouter: The configured router with all routes included
    """
    return api_router
