from fastapi import FastAPI

from app.routers import cafes

app = FastAPI()
app.include_router(cafes.router)

@app.get("/")
def root():
    return {"status": "ok"}

from app.core.database import engine
from sqlalchemy import text

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"database": "connected"}