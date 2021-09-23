from typing import Optional

from pydantic import BaseModel


class NoticeBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]


class NoticeCreate(NoticeBase):
    name: str
    price: float


class NoticeUpdate(NoticeBase):
    id: int
    pass


class NoticeResponse(NoticeBase):
    class Config:
        orm_mode = True
