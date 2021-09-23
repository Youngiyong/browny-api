from http.client import HTTPException
from typing import Any, Dict, Optional, Union, List, Type
from datetime import datetime
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.members import Members, MemberFollows, MemberProfiles
from app.schemas.members import MemberBase, MemberCreate, MemberFollow, MemberProfile, MemberResponse, MemberProfileCreate, MemberProfileUpdate, MemberFollowCreate, MemberFollowUpdate


class CRUDMember(CRUDBase[Members, MemberCreate, MemberFollow]):

    def __init__(self, model: Type[Members]):
        self.model = model

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100 ) -> List[Members]:
        db_list_obj = db.query(self.model).filter(self.model.deleted_at==None).all()
        return db_list_obj

    def get(self, db: Session, id: Any) -> Optional[Members]:
        return db.query(self.model).filter(self.model.id == id, self.model.deleted_at == None).first()

    def delete(self, db: Session, db_obj: Members) -> Optional[Members]:
        db_obj.deleted_at = datetime.now()
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def create(self, db: Session, payload: MemberCreate) -> Members:
        try:
            member_obj = self.model(
                name=payload.name,
                email=payload.email,
                sex=payload.sex,
                password=payload.password,
                phone=payload.phone,
                birthday=payload.birthday
            )

            db.add(member_obj)
            db.commit()
            db.refresh(member_obj)

            member_profile_obj = MemberProfiles(
                member_id=member_obj.id,
                name=payload.name
            )
            db.add(member_profile_obj)
            db.commit()
            return member_obj
        except:
            raise HTTPException(status_code=500, detail="Internal Error")
            db.rollback()


    def update(
        self, db: Session, *, db_obj: Members, obj_in: Union[MemberCreate, Dict[str, Any]]
    ) -> Members:

        return super().update(db, db_obj=db_obj, obj_in=obj_in)


class CRUDBMemberProfile(CRUDBase[MemberProfiles, MemberProfileCreate, MemberProfileUpdate]):

    def __init__(self, model: Type[MemberProfiles]):
        self.model = model

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100 ) -> List[MemberProfiles]:
        db_list_obj = db.query(self.model).all()
        return db_list_obj

    def get(self, db: Session, id: Any) -> Optional[MemberProfiles]:
        return db.query(self.model).filter(self.model.id == id).first()

    def update(
        self, db: Session, *, db_obj: MemberProfiles, obj_in: Union[MemberProfileUpdate, Dict[str, Any]]
    ) -> MemberProfiles:
        db_obj.updated_at = datetime.now()
        return super().update(db, db_obj=db_obj, obj_in=obj_in)


class CRUDMemberFollow(CRUDBase[MemberFollows, MemberFollowCreate, MemberFollowUpdate]):

    def __init__(self, model: Type[MemberFollows]):
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[MemberFollows]:
        return db.query(self.model).filter(self.model.id == id).first()

    def remove(self, db: Session, db_obj: MemberFollows):
        db.delete(db_obj)
        db.commit()
        return db_obj

    def create(self, db: Session, payload: MemberFollowCreate) -> MemberFollows:
        try:
            member_follow_obj = self.model(
                member_id=payload.member_id,
                follow_id=payload.follow_id,
                memo=payload.memo
            )

            db.add(member_follow_obj)
            db.commit()
            db.refresh(member_follow_obj)

            return member_follow_obj

        except:
            raise HTTPException(status_code=500, detail="Internal Error")
            db.rollback()


member = CRUDMember(Members)
member_profile = CRUDBMemberProfile(MemberProfiles)
member_follow = CRUDMemberFollow(MemberFollows)
