from fastapi import HTTPException, status
from sqlmodel import Session
from app.product.service import ProductService
from app.utils.logger_class import LoggerClass
from typing import List, Dict

class ProductController:
    @staticmethod
    async def get_on_sale_products(db: Session) -> List[Dict]:
        """
        Get on sale products.
        """
        try:
            products_list = await ProductService.get_on_sale_products(db)

            if not products_list:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="No on sale products found"
                )

            serialized_products = [product.model_dump() for product in products_list]
            return serialized_products

        except HTTPException as http_exc:
            # Re-raise HTTPExceptions (like the 404)
            raise http_exc
        except Exception as e:  
            db.rollback()
            LoggerClass.error(f"Error getting on sale products: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Internal Server Error: {e}"
            )