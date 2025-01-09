from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.database.conn import engine, session
from app.database import models

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
