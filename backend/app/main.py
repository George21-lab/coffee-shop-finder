from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import engine
from app.routers import cafes, auth

app = FastAPI()

app.include_router(cafes.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"database": "connected"}