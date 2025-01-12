from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database.conn import engine, session
from app.database import models
import json
import requests
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

# POST /rolled; body: {bid: int, uid: int}
@app.post('/rolled')
async def rolled(requests, db: Session = get_db()):
    requests = json.loads(requests)
    bicycle = db.query(models.Bicycle).filter(models.Bicycle.bid == requests['body'].bid).first()
    user = db.query(models.User).filter(models.User.uid == requests['body'].uid).first()
    if bicycle is None:
        raise HTTPException(status_code=404, detail="Bicycle not found")
    if bicycle.status == "rolled":
        pass # 이 부분에 임베디드와 통신해서 올바로 세워졌는지 확인하는 코드 추가
        bicycle.status = "available"
        db.commit()
        if not user.daylimit:
            return {"message": f"Bicycle {bicycle.bid}is available now"}
        give_coupon(user.uid, name="ThankToRolling", code="THANKYOUTOROLL", value=10)
        user.daylimit -= 1
        db.commit()
        return {"message": f"Bicycle {bicycle.bid}is available now"}
        

def give_coupon(uid: int, code: str, name: str, value: int, type: str = "percent"):
    db = session()
    coupon = models.Coupons(uid=uid, name=name, description="Thank you", code=code, value=value, type=type)
    db.add(coupon)
    db.commit()


@app.get("/score1")
async def func1():
    sample_data = [10, 30, 90, -50, 70]
    return score1(sample_data)
