from typing import Any, List
from starlette.requests import Request
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jwt import encode
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token
from pydantic import BaseModel, Field
from app import schemas, crud
from app.core.deps import get_db

router = APIRouter()


@router.get("/login")
def login(request: Request) -> Any:
    """
    Retrieve all products.
    """
    pass
