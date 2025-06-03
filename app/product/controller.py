from fastapi import HTTPException, status, UploadFile
from sqlmodel import Session
from app.product.service import ProductService
from app.utils.logger_class import LoggerClass
from typing import List, Dict
from sqlalchemy.exc import IntegrityError
from app.schemas.response_model import DefaultResponse
import json


class ProductController:
    
    @staticmethod
    def get_not_on_sale_products(db: Session, page_number: int, page_size: int) -> List[Dict]:
        """
        Get not on sale products.
        """
        try:
            skip = (page_number - 1) * page_size
            products_list = ProductService.get_not_on_sale_products(db, skip, page_size)
            
            if not products_list:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="No products found"
                )
            
            serialized_products = [product.model_dump() for product in products_list]
            return DefaultResponse(data=serialized_products, message="Products retrieved successfully")

        except HTTPException as http_exc:  
            # Re-raise HTTPExceptions (like the 404)
            raise http_exc
        except Exception as e:
            LoggerClass.error(f"Error getting products: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {e}"
            )


    @staticmethod
    def get_on_sale_products(db: Session, page_number: int, page_size: int) -> List[Dict]:
        """
        Get on sale products.
        """
        try:
            skip = (page_number - 1) * page_size
            products_list = ProductService.get_on_sale_products(db, skip, page_size)  

            if not products_list:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="No on sale products found"
                )

            serialized_products = [product.model_dump() for product in products_list]
            return DefaultResponse(data=serialized_products, message="Products retrieved successfully")

        except HTTPException as http_exc:
            # Re-raise HTTPExceptions (like the 404)
            raise http_exc
        except Exception as e:  
            LoggerClass.error(f"Error getting on sale products: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {e}"
            )

    @staticmethod
    async def import_products_fast(db: Session, file: UploadFile) -> DefaultResponse:
        """
        Bulk insert products into the database.
        """
        try:
            content = await file.read()
            products = json.loads(content)

            if not isinstance(products, list):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid JSON format. Expected a list of products."
                )

            await ProductService.bulk_insert_products(db, products)
            return DefaultResponse(data=None, message="Products imported successfully")

        except IntegrityError as e:
            db.roolback()
            LoggerClass.error(f"Error importing products: {e}")
            raise ValueError("One or more products violate unique constraints.")
        except Exception as e:
            db.rollback()
            LoggerClass.error(f"Error importing products: {e}")
            raise HTTPException(
                status_code = 500,
                detail=f"Failed to import products: {e}"
            )

    @staticmethod
    def get_product_by_id(db: Session, id: int):
        """
        Get a product by its ID.
        """
        try:
            product = ProductService.get_product_by_id(db, id)
            if not product:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
                )
            serialized_product = product.model_dump()
            return DefaultResponse(data=serialized_product, message="Product retrieved successfully")
        
        except HTTPException as http_exc:
            # Re-raise HTTPExceptions (like the 404)
            raise http_exc
        except Exception as e:
            LoggerClass.error(f"Error getting product by id: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {e}"
            )

    @staticmethod
    def get_barcodes(db: Session):
        """
        Get all products in database, seleting barcode
        """
        try:
            barcodes = ProductService.get_barcodes(db)
            return DefaultResponse(data=barcodes, message="Barcodes retrieved successfully")
        except Exception as e:
            LoggerClass.error(f"Error getting barcodes: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {e}"
            )
    @staticmethod
    def get_embeddings(db: Session):
        """
        Get all products in database, seleting embeddings
        """
        try:
            embeddings = ProductService.get_embeddings(db)
            return DefaultResponse(data=embeddings, message="Embeddings retrieved sucessfully")
        except Exception as e:
            LoggerClass.error(f"Error getting embeddings: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {e}"
            )


