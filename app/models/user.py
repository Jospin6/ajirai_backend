import uuid
from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID

class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(index=True, unique=True)
    username: Optional[str] = None
    avatar: Optional[str] = None
    sub: Optional[str] = None
    hashed_password: str