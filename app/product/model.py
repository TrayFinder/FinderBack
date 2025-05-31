from sqlalchemy import Column, JSON, LargeBinary
from sqlmodel import Field
from app.schemas.entity_model import Base
from typing import Optional, List


class Product(Base, table=True):
    """
    Represents a product in the database.
    """

    id: Optional[int] = Field(default=None, primary_key=True)

    filename: str = Field(nullable=False)
    
    barcode: str = Field(nullable=False, unique=True)

    product_name: str = Field(nullable=False, max_length=255)

    description: Optional[str] = Field(default=None)

    category: str = Field(default=None, max_length=30)

    subcategory: str = Field(default=None, max_length=30)

    price: float = Field(nullable=False)

    sale_price: float = Field(default=None)

    sale_percentage: Optional[int] = Field(default=None)

    stock: int = Field(default=None)

    on_sale: bool = Field(default=None)

    embeddings: Optional[List[float]] = Field(default=None, sa_column=Column(JSON, nullable=True))
