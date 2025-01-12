from sqlalchemy.orm import Session
from app.database.conn import engine, session
from app.database import models

db = session()
all_users = db.query(models.User).all()
for user in all_users:
    user.daylimit = 3
    db.commit()