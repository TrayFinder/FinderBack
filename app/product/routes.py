from typing import List

from fastapi import APIRouter, Depends, File, Path, Query, UploadFile
from sqlmodel import Session

from app.core.database import get_session
from app.product.controller import ProductController
from app.schemas.response_model import DefaultResponse

router = APIRouter(prefix='/products', tags=['Products'])


@router.post('/upload-json', response_model=DefaultResponse)
async def import_products_fast(
    db: Session = Depends(get_session), file: UploadFile = File(...)
):
    return await ProductController.import_products_fast(db, file)


@router.post('/upload-image', response_model=DefaultResponse)
async def upload_image(file: UploadFile = File(...)):
    return await ProductController.upload_image_and_convert_to_array(file)


@router.get('/not-sale', response_model=DefaultResponse)
def get_products(
    db: Session = Depends(get_session),
    page_number: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
):
    return ProductController.get_not_on_sale_products(
        db, page_number, page_size
    )


@router.get('/sale', response_model=DefaultResponse)
def get_on_sale_products(
    db: Session = Depends(get_session),
    page_number: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
):
    return ProductController.get_on_sale_products(db, page_number, page_size)


@router.get('/barcodes', response_model=DefaultResponse)
def get_barcodes(db: Session = Depends(get_session)):
    return ProductController.get_barcodes(db)


@router.get('/embeddings', response_model=DefaultResponse)
def get_embeddings(db: Session = Depends(get_session)):
    return ProductController.get_embeddings(db)


@router.get('/{id}', response_model=DefaultResponse)
def get_product_by_id(
    db: Session = Depends(get_session),
    id: int = Path(..., ge=1, description='The ID of the product to get'),
):
    return ProductController.get_product_by_id(db, id)
