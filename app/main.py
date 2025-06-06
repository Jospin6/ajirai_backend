from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.db import init_db
from app.routes.user import router as user_router
from app.routes.chat import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield

app = FastAPI(title="FastAPI with PostgreSQL", lifespan=lifespan, version="0.1")

app.include_router(user_router, prefix="/api/users", tags=["users"])
app.include_router(chat_router, prefix="/api/chat", tags=["chat"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
