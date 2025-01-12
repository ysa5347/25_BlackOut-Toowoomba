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

@app.post("/score")
async def score(requests):
    requests = json.loads(requests)
    transaction = db.query(models.Transaction).filter(models.Transaction.id == requests['body'].id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    transaction.score = requests['body'].score
    db.commit()
    return {"message": "Score updated"}

Class Transaction(BaseModel):
    uid: int,
    bid: int,
    cid: int,
    start_lat: float,
    start_lng: float,
    created_at: datetime.datetime,
    updated_at: datetime.datetime,
    status: str,
    start_time: datetime.datetime

# POST /user; body: {uid: int, email: str, hashed_password: str, exp: int, level: int, score: int, daylimit: int, friends_list: list, is_active: bool, is_superuser: bool}
@app.get("/transaction/{id}")
async def get_transaction(id: str, db: Session = get_db()):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

# POST /transaction; body: {uid: int, bid: int, }
@app.post("/transaction")
async def transaction(requests, db: Session = get_db()):
    requests = json.loads(requests)
    user = db.query(models.User).filter(models.User.uid == requests['body'].uid).first()
    bicycle = db.query(models.Bicycle).filter(models.Bicycle.bid == requests['body'].bid).first()
    if user is None or bicycle is None:
        raise HTTPException(status_code=404, detail="User or Bicycle not found")
    if not user.daylimit:
        raise HTTPException(status_code=400, detail="You have no daylimit")
    tr = models.Transaction(uid=requests['body'].uid, bid=requests['body'].bid, cid=requests['body'].cid, start_lat=requests['body'].start_lat, start_lng=requests['body'].start_lng, created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), status="pending")
    db.add(transaction)
    db.commit()
    return {"message": "Transaction created"}

# peering search request API
# GET /transaction/peering; body: {id: str}
@app.get("/transaction/peering")
async def peering(requests):
    requests = json.loads(requests)
    transaction = db.query(models.Transaction).filter(models.Transaction.id == requests['body'].id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    peer_transactions = db.query(models.Transaction).filter((models.Transaction.start_lat - transaction.start_lat < 0.0001) and (models.Transaction.start_lng - transaction.start_lng < 0.0001)).all()
    friends_transactions = peer_transactions.filter(models.Transaction.uid in db.query(models.Friends).filter(models.Friends.uid == transaction.uid).all())
    return {[transaction.id for transaction in friends_transactions]}


@app.get("/score1")
async def func1():
    sample_data = [10, 30, 90, -50, 70]
    return score1(sample_data)
