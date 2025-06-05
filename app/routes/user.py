from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.user_schema import UserCreate, UserRead
from app.controllers.user import create_user, delete_user, get_all_users, get_user_by_email, get_user_by_id, update_user
from app.config.db import get_session

router = APIRouter()

@router.post("/", response_model=UserRead)
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    existing = get_user_by_email(user.email, session)
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    return create_user(user, session)

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: UUID, session: Session = Depends(get_session)):
    user = get_user_by_id(user_id, session)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[UserRead])
def get_users(session: Session = Depends(get_session)):
    users = get_all_users(session)
    return users

@router.put("/{user_id}", response_model=UserRead)
def update_a_user(user_id: UUID, user: UserCreate, session: Session = Depends(get_session)):
    existing_user = get_user_by_email(user.email, session)
    if existing_user and existing_user.id != user_id:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    updated_user = update_user(user_id, user, session)
    return updated_user

@router.delete("/{user_id}")
def delete_a_user(user_id: UUID, session: Session = Depends(get_session)):
    try:
        delete_user(user_id, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"detail": "User deleted successfully"}