from sqlalchemy import Column, DateTime, LargeBinary
from sqlmodel import Field
from app.schemas.entity_model import Base
from datetime import datetime, timezone
from typing import Optional

class Product(Base, table=True):
    """
    Represents a product in the database.
    """

    id: Optional[int] = Field(default=None, primary_key=True)

    name: str = Field(nullable=False, max_length=255)

    description: Optional[str] = Field(default=None)

    category: Optional[str] = Field(default=None, max_length=30)

    subcategory: Optional[str] = Field(default=None, max_length=30)

    price: float = Field(nullable=False)

    stock: Optional[int] = Field(default=None)

    sale: Optional[bool] = Field(default=None)

    byte_image: Optional[bytes] = Field(default=None, sa_column=Column(LargeBinary, nullable=True))
