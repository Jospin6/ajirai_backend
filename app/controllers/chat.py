from sqlmodel import Session, select
from models.chat import ChatSession, Message
from datetime import datetime
from uuid import UUID


def get_or_create_chat_session(user_id: UUID, db: Session) -> ChatSession:
    session_stmt = select(ChatSession).where(ChatSession.user_id == user_id).order_by(ChatSession.created_at.desc())
    existing = db.exec(session_stmt).first()
    
    if existing:
        return existing

    new_session = ChatSession(user_id=user_id)
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session


def save_user_message(session_id: UUID, content: str, db: Session) -> Message:
    message = Message(
        session_id=session_id,
        role="user",
        content=content
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def save_ai_response(session_id: UUID, content: str, db: Session) -> Message:
    message = Message(
        session_id=session_id,
        role="assistant",
        content=content
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message
