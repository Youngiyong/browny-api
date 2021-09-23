from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class BlogBase(BaseModel):
    id: Optional[int]
    member_id: Optional[int]
    name: Optional[str]
    blog_url: Optional[str]
    blog_icon: Optional[str]
    blog_favicon: Optional[str]
    created_at: Optional[datetime]


class BlogCreate(BaseModel):
    member_id: Optional[int]
    name: Optional[str]
    blog_url: Optional[str]
    blog_icon: Optional[str]
    blog_favicon: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "member_id": 1,
                "name": "This is Blog name",
                "blog_url": "https://www.example.com",
                "blog_icon": "blogs/2021092012345678.png",
                "blog_favicon": "blogs/202109203929012910.png",
            }
        }


class BlogUpdate(BaseModel):
    name: Optional[str]
    blog_url: Optional[str]
    blog_icon: Optional[str]
    blog_favicon: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "This is Blog name",
                "blog_url": "https://www.example.com",
                "blog_icon": "blogs/2021092012345678.png",
                "blog_favicon": "blogs/202109203929012910.png",
            }
        }


class BlogResponse(BlogBase):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id" : 1,
                "member_id": 1,
                "name": "This is Blog name",
                "blog_url": "https://www.example.com",
                "blog_icon": "blogs/2021092012345678.png",
                "blog_favicon": "blogs/202109203929012910.png",
                "created_at": datetime.now()
            }
        }


class BlogLikeBase(BaseModel):
    id: Optional[int]
    blog_id: Optional[int]
    member_id: Optional[int]
    created_at: Optional[datetime]


class BlogLike(BlogLikeBase):
    id: int

    class Config:
        orm_mode = True


class Blog(BlogBase):
    id = int
    blog_likes: List[BlogLike] = []

    class Config:
        orm_mode = True


class BlogLikeCreate(BlogLikeBase):
    blog_id: Optional[int]
    member_id: Optional[int]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "blog_id": 1,
                "member_id": 1
            }
        }


class BlogLikeUpdate(BlogLikeBase):
    blog_id: Optional[int]
    member_id: Optional[int]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "blog_id": 1,
                "member_id": 1
            }
        }


class BlogLikeResponse(BlogLikeBase):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id" : 1,
                "blog_id": 1,
                "member_id": 1,
                "name": "This is Blog name",
                "created_at": datetime.now()
            }
        }
