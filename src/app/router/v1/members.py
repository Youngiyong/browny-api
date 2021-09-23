from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, crud
from app.core.deps import get_db

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.MemberResponse)
def create_member(*, db: Session = Depends(get_db), payload: schemas.MemberCreate) -> Any:
    """
    Create Members
    """
    member = crud.member.create(db, payload=payload)
    return member


@router.delete("{id}", status_code=status.HTTP_200_OK)
def remove_member(*, db: Session = Depends(get_db), id: int) -> Any:
    """
    Delete Members
    """
    member = crud.member.get(db, id=id)

    if not member:
        raise HTTPException(status_code=404, detail="member not found")
    crud.member.delete(db, db_obj=member)


@router.post("/follows", status_code=status.HTTP_201_CREATED, response_model=schemas.MemberFollowResponse)
def create_member_follow(*, db: Session = Depends(get_db), payload: schemas.MemberFollowCreate) -> Any:
    member_follow = crud.member_follow.create(db, payload=payload)
    return member_follow


@router.delete("/follows/{id}", status_code=status.HTTP_200_OK)
def delete_member_follow(*, db: Session = Depends(get_db), id: int) -> Any:
    member_follow = crud.member_follow.get(db, id=id)
    if not member_follow:
        raise HTTPException(status_code=404, detail="member_follow id not found")

    crud.member_follow.remove(db=db, db_obj=member_follow)


@router.put("/profiles/{id}", status_code=status.HTTP_200_OK)
def update_member_profile(*, db: Session = Depends(get_db), id: int, payload: schemas.MemberProfileUpdate) -> Any:
    member_profile = crud.member_profile.get(db, id=id)
    if not member_profile:
        raise HTTPException(status_code=404, detail="member_profile id not found")

    crud.member_profile.update(db=db, db_obj=member_profile, obj_in=payload)