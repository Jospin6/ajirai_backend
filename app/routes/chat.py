from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.db import get_session 
from schemas.chat import AskInput, AskResponse
from controllers.chat import (
    get_or_create_chat_session,
    save_user_message,
    save_ai_response
)

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
def ask(input: AskInput, db: Session = Depends(get_session)):
    session = get_or_create_chat_session(input.user_id, db)

    save_user_message(session.id, input.content, db)

    # Remplace cette réponse par une vraie IA (OpenAI, Ollama, etc.)
    ai_reply = f"Voici une réponse automatique à : \"{input.content}\""
    save_ai_response(session.id, ai_reply, db)

    return AskResponse(
        session_id=session.id,
        user_message=input.content,
        ai_response=ai_reply
    )
