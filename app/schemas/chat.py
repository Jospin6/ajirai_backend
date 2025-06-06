from pydantic import BaseModel
from uuid import UUID

class AskInput(BaseModel):
    user_id: int
    content: str

class AskResponse(BaseModel):
    session_id: UUID
    user_message: str
    ai_response: str
