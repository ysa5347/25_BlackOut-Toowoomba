from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Boolean, Enum, Text
from app.database.conn import base

class User(base):
    __tablename__ = "user"

    uid = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))

    exp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    score = Column(Integer, default=100)

    daylimit = Column(Integer, default=3)

    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

class Coupons(base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(Text)
    code = Column(String(255), index=True)
    type = Column(Enum("percent", "amount"), default="percent")
    value = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    used_at = Column(DateTime)
    uid = Column(Integer, ForeignKey('user.uid'))

class Bicycle(base):
    __tablename__ = "bicycles"

    bid = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(Text)
    type = Column(Enum("GCOO", "GBike"), default="GCOO")
    status = Column(Enum("available", "rented", "maintenance", "rolled"), default="available")
    is_available = Column(Boolean, default=True)
    is_discounted = Column(Boolean, default=False)
    discount = Column(Integer, default=0)
    image = Column(String(255))                         # S3 bucket object key; img/bike-<image>
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime, nullable=True)
x
class Transaction(base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, index=True)                       # s3 bucket object key; Trans-<id>
    uid = Column(Integer, ForeignKey('user.uid'))
    bid = Column(Integer, ForeignKey('bicycles.id'))
    cid = Column(Integer, ForeignKey('coupons.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    start_lat = Column(Float)
    start_lng = Column(Float)
    end_lat = Column(Float, nullable=True)
    end_lng = Column(Float, nullable=True)
    start_time = Column(DateTime)
    status = Column(Enum("active", "completed", "cancelled", "refunded", "pending"), default="pending")
    is_active = Column(Boolean, default=True)
    is_completed = Column(Boolean, default=False)
    is_cancelled = Column(Boolean, default=False)
    is_refunded = Column(Boolean, default=False)
    is_reviewed = Column(Boolean, default=False)
    review = Column(Text)
    rating = Column(Integer)