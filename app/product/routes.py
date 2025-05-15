from fastapi import APIRouter
from sqlmodel import Session
from app.schemas.response_model import DefaultResponse
from app.product.controller import ProductController

router= APIRouter(prefix="/products", tags=["Products"])

@router.get("/sale", model_response= DefaultResponse)
async def get_on_sale_products(db: Session):
    return await ProductController.get_on_sale_products()
