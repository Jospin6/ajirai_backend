from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID

class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    username: str
    hashed_password: str