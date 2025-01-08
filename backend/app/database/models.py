from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Enum, Text
from app.database.conn import base

class User(base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)