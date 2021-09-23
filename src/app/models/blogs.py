from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class Blogs(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100), nullable=False)
    blog_url = Column(String(length=100), nullable=True)
    blog_icon = Column(String(length=100), nullable=True)
    blog_favicon = Column(String(length=100), nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    # member = relationship("Members", back_populates="id")
    blog_likes = relationship("BlogLikes", back_populates="blogs")


class BlogLikes(Base):
    __tablename__ = "blog_likes"
    id = Column(Integer, primary_key=True, index=True)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    member_id = Column(Integer, ForeignKey("members.id"))
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    blogs = relationship("Blogs", back_populates="blog_likes")
