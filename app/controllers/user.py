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
