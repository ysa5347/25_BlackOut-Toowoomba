from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.database.conn import engine, session
from app.database import models
from utils.func1 import score1

models.base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/score1")
async def func1():
    sample_data = [10, 30, 90, -50, 70]
    return score1(sample_data)
