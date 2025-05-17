from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from app.schemas.response_model import DefaultResponse
from app.product.controller import ProductController
from app.core.database import get_session

router= APIRouter(prefix="/products", tags=["Products"])


@router.get("/not_sale", response_model= DefaultResponse)
async def get_products(
    db: Session = Depends(get_session),
    page_number: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100)
):
    return await ProductController.get_not_on_sale_products(db, page_number, page_size)

@router.get("/sale", response_model= DefaultResponse)
async def get_on_sale_products(
    db: Session = Depends(get_session),
    page_number: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100)
):
    return await ProductController.get_on_sale_products(db, page_number, page_size)
