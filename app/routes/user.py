from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.user_schema import UserCreate, UserRead
from app.controllers.user import create_user, get_user_by_email
from app.config.db import get_session

router = APIRouter()

@router.post("/", response_model=UserRead)
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    existing = get_user_by_email(user.email, session)
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    return create_user(user, session)