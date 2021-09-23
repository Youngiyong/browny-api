from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, crud
from app.core.deps import get_db

router = APIRouter()


@router.get("")
def find_all_blogs(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve all products.
    """
    pass
