import datetime
from typing import Any, Dict, Optional, Union, List, Type

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.blogs import Blogs, BlogLikes
from app.schemas.blogs import BlogCreate, BlogUpdate, BlogLikeCreate, BlogLikeUpdate


class CRUDBlog(CRUDBase[Blogs, BlogCreate, BlogUpdate]):

    def __init__(self, model: Type[Blogs]):
        self.model = model

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100 ) -> List[Blogs]:
        db_list_obj = db.query(self.model).filter(self.model.deleted_at==None).all()
        return db_list_obj

    def get(self, db: Session, id: Any) -> Optional[Blogs]:
        return db.query(self.model).filter(self.model.id == id, self.model.deleted_at == None).first()

    def delete(self, db: Session, db_obj: Blogs) -> Optional[Blogs]:
        db_obj.deleted_at = datetime.datetime.now()
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def create(self, db: Session, *, payload: BlogCreate) -> Blogs:
        db_obj = self.model(
            member_id=payload.member_id,
            name=payload.name,
            blog_url=payload.blog_url,
            blog_icon=payload.blog_icon,
            blog_favicon=payload.blog_favicon
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Blogs, obj_in: Union[BlogUpdate, Dict[str, Any]]
    ) -> Blogs:

        return super().update(db, db_obj=db_obj, obj_in=obj_in)


class CRUDBlogLike(CRUDBase[BlogLikes, BlogLikeCreate, BlogLikeUpdate]):
    def __init__(self, model: Type[BlogLikes]):
        self.model = model

    def create(self, db: Session, *, payload: BlogLikeCreate) -> BlogLikes:
        db_obj = self.model(
            blog_id=payload.blog_id,
            member_id=payload.member_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, id: Any, blog_id: Any) -> Optional[BlogLikes]:
        return db.query(self.model).filter(self.model.id == id and self.model.blog_id == blog_id).first()

    def remove(self, db: Session, db_obj: BlogLikes):
        db.delete(db_obj)
        db.commit()
        return db_obj


blog = CRUDBlog(Blogs)

blog_like = CRUDBlogLike(BlogLikes)
