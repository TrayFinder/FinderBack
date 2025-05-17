from sqlmodel import Session, select
from app.utils.logger_class import LoggerClass
from app.product.model import Product
from typing import List, Optional

class ProductService:
    """Service class for product-related operations."""

    @staticmethod
    async def get_not_on_sale_products(db: Session, skip: int, limit: int) -> List[Optional[Product]]:
        """
        Get all products in database.
        """
        stmt = select(Product).where(Product.sale == False).offset(skip).limit(limit)
        products_list = db.exec(stmt).all()

    @staticmethod
    async def get_on_sale_products(db: Session, skip: int, limit: int) -> List[Optional[Product]]:
        """
        Get on sale products in database.
        """
        stmt = select(Product).where(Product.sale == True).offset(skip).limit(limit)
        products_list = db.exec(stmt).all()
        LoggerClass.debug(f"Number of on sale products found: {products_list}")
        return products_list