from fastapi import HTTPException, status
from sqlmodel import Session
from app.product.service import ProductService
from app.utils.logger_class import LoggerClass
from typing import List, Dict
from app.schemas.response_model import DefaultResponse


class ProductController:
    
    @staticmethod
    async def get_not_on_sale_products(db: Session, page_number: int, page_size: int) -> List[Dict]:
        """
        Get all products.
        """
        try:
            skip = (page_number - 1) * page_size
            products_list = await ProductService.get_not_on_sale_products(db, skip, page_size)
            
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
            db.rollback()
            LoggerClass.error(f"Error getting products: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {e}"
            )


    @staticmethod
    async def get_on_sale_products(db: Session, page_number: int, page_size: int) -> List[Dict]:
        """
        Get on sale products.
        """
        try:
            skip = (page_number - 1) * page_size
            products_list = await ProductService.get_on_sale_products(db, skip, page_size)

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
            db.rollback()
            LoggerClass.error(f"Error getting on sale products: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {e}"
            )