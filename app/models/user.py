from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    user = "user"

class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(index=True, unique=True)
    username: Optional[str] = None
    avatar: Optional[str] = None
    sub: Optional[str] = None
    hashed_password: str
    role: UserRole = Field(default=UserRole.user)
    is_active: bool = Field(default=True)