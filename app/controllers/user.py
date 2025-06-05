from sqlmodel import Session, select
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password

def create_user(user_data: UserCreate,session: Session) -> User:
    user = User(
        email=user_data.email,
        username=user_data.username,
        hashed_password=hash_password(user_data.password)
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user_by_email(email: str, session: Session) -> User | None:
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

def get_user_by_id(user_id: str, session: Session) -> User | None:
    statement = select(User).where(User.id == user_id)
    return session.exec(statement).first()

def get_all_users(session: Session) -> list[User]:
    statement = select(User)
    return session.exec(statement).all()

def update_user(user_id: str, user_data: UserCreate, session: Session) -> User:
    user = get_user_by_id(user_id, session)
    if not user:
        raise ValueError("User not found")
    
    user.email = user_data.email
    user.username = user_data.username
    user.hashed_password = hash_password(user_data.password)
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_user(user_id: str, session: Session) -> None:
    user = get_user_by_id(user_id, session)
    if not user:
        raise ValueError("User not found")
    session.delete(user)
    session.commit()