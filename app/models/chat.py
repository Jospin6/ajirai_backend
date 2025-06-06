from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from uuid import UUID, uuid4


class ChatSession(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID
    title: str = Field(default="New chat")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    messages: List["Message"] = Relationship(back_populates="session")


class Message(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    session_id: UUID = Field(foreign_key="chatsession.id")
    role: str = Field(regex="^(user|assistant|system)$")
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    session: Optional[ChatSession] = Relationship(back_populates="messages")
