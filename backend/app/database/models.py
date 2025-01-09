from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Enum, Text
from app.database.conn import base

class User(base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
