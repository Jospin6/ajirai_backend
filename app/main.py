from fastapi import FastAPI
# from app.routes.item_route import router as item_router
from contextlib import asynccontextmanager
from app.config.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield

app = FastAPI(title="FastAPI with PostgreSQL", lifespan=lifespan, version="0.1")


# app.include_router(item_router, prefix="/api/v1/items", tags=["items"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
