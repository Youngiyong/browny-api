
from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    id: Optional[int]
    member_id: Optional[int]
    blog_url: Optional[str]
    blog_icon: Optional[str]
    blog_favicon: Optional[str]


class PostCreate(PostBase):
    member_id: Optional[int]
    blog_url: Optional[str]
    blog_icon: Optional[str]
    blog_favicon: Optional[str]


class PostUpdate(PostBase):
    id: int
    pass


class PostResponse(PostBase):
    class Config:
        orm_mode = True
