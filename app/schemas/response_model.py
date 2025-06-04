from typing import Optional, Any
from pydantic import BaseModel


class DefaultResponse(BaseModel):
    """Resposta padrão para endpoints da API."""

    data: Optional[Any] = None
    message: Optional[str] = None
