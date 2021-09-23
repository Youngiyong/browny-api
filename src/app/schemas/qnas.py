from typing import Optional
from pydantic import BaseModel


class QNASBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]


class QNASCreate(QNASBase):
    name: str
    price: float


class QNASUpdate(QNASBase):
    id: int
    pass


class QNASResponse(QNASBase):
    class Config:
        orm_mode = True
