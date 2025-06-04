from datetime import datetime
from typing import Any, Dict, Type, TypeVar
from sqlalchemy.sql import func as sa_func
from sqlmodel import SQLModel, Field

T = TypeVar('T', bound='Base')   # usado nos métodos de ajuda


class DeclarativeBase(SQLModel):
    """Base comum para todos os modelos ― configurações Pydantic ficam aqui."""

    __abstract__ = True

    model_config = {
        'from_attributes': True,  # habilita .from_orm()
        'populate_by_name': True,
        'arbitrary_types_allowed': True,  # útil p/ objetos complexos
    }


class TimestampMixin(SQLModel):
    created_at: datetime = Field(
        default=None,
        nullable=False,
        sa_column_kwargs={'server_default': sa_func.now()},
        description='Momento (UTC) em que o registro foi criado',
    )

    updated_at: datetime = Field(
        default=None,
        nullable=False,
        sa_column_kwargs={
            'server_default': sa_func.now(),
            'onupdate': sa_func.now(),
        },
        description='Momento (UTC) da última modificação',
    )


class Base(DeclarativeBase, TimestampMixin):
    """Modelo raiz para todas as entidades."""

    __abstract__ = True

    @classmethod
    def from_dict(cls: Type[T], data: Dict[str, Any]) -> T:
        """
        Constrói o objeto validando tudo via Pydantic.
        Usa `model_validate` (Pydantic v2) e lida com ISO 8601 automaticamente.
        """
        return cls.model_validate(data)

    def update_from_dict(self, data: Dict[str, Any]) -> None:
        """
        Atualiza atributos permitidos.
        """
        for field, value in data.items():
            if hasattr(self, field):
                setattr(self, field, value)
