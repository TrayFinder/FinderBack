from sqlmodel import Session, select
from app.utils.logger_class import LoggerClass
from app.product.model import Product
from typing import List, Optional
from PIL import Image
import numpy as np
import io
from fastapi import UploadFile

class ProductService:
    """Service class for product-related operations."""

    @staticmethod
    def get_not_on_sale_products(db: Session, skip: int, limit: int) -> List[Optional[Product]]:
        """
        Get all products in database.
        """
        stmt = select(Product).where(Product.on_sale == False).offset(skip).limit(limit)
        products_list = db.exec(stmt).all()
        LoggerClass.debug(f"Number of not on sale products found: {len(products_list)}")
        return products_list

    @staticmethod
    def get_on_sale_products(db: Session, skip: int, limit: int) -> List[Optional[Product]]:
        """
        Get on sale products in database.
        """
        stmt = select(Product).where(Product.on_sale == True).offset(skip).limit(limit)
        products_list = db.exec(stmt).all()
        LoggerClass.debug(f"Number of on sale products found: {len(products_list)}")
        return products_list

    @staticmethod
    async def bulk_insert_products(db: Session, products: List[dict]) -> None:
        """
        Bulk insert products into the database.
        """
        db_products = [Product(**product) for product in products]
        db.add_all(db_products)
        db.commit()

    @staticmethod
    def get_product_by_id(db: Session, id: int) -> Optional[Product]:
        """
        Get a product by its ID.
        """
        stmt = select(Product).where(Product.id == id)
        product = db.exec(stmt).first()
        LoggerClass.debug(f"Product found with id {id}: {product is not None}")
        return product

    @staticmethod
    def get_barcodes(db: Session) -> List[str]:
        """
        Get all products in database, seleting barcode
        """
        stmt = select(Product.barcode).order_by(Product.id)
        barcode_list = db.exec(stmt).all()
        return barcode_list

    @staticmethod
    def get_embeddings(db: Session) -> List[str]:
        """
        Get all products in database, seleting embeddings
        """ 
        stmt = select(Product.embeddings).order_by(Product.id)
        embeddings_list = db.exec(stmt).all()
        return embeddings_list
    
    @staticmethod
    async def image_to_numpy_array(file: UploadFile) -> np.ndarray:
        """
        Converts an uploaded image file to a NumPy array.
        """ 
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image_array = np.array(image)
        return image_array
