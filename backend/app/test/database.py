from faker import Faker
import random
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models import User, Coupons, Bicycle, Transaction

fake = Faker()

def create_test_data(session: Session):
    # Generate test data for User
    for _ in range(20):
        user = User(
            email=fake.unique.email(),
            hashed_password=fake.password(),
            exp=random.randint(0, 1000),
            level=random.randint(1, 10),
            score=random.randint(50, 500),
            daylimit=random.randint(1, 5),
            is_active=random.choice([True, False]),
            is_superuser=random.choice([True, False])
        )
        session.add(user)

    # Generate test data for Coupons
    for _ in range(20):
        coupon = Coupons(
            name=fake.word(),
            description=fake.text(),
            code=fake.unique.uuid4(),
            type=random.choice(["percent", "amount"]),
            value=random.randint(10, 50),
            is_active=random.choice([True, False]),
            created_at=fake.date_time_between(start_date="-1y", end_date="now"),
            used_at=None if random.choice([True, False]) else fake.date_time_between(start_date="-1y", end_date="now"),
            uid=random.randint(1, 20)
        )
        session.add(coupon)

    # Generate test data for Bicycle
    for _ in range(20):
        bicycle = Bicycle(
            name=fake.word(),
            description=fake.text(),
            type=random.choice(["GCOO", "GBike"]),
            status=random.choice(["available", "rented", "maintenance", "rolled"]),
            is_available=random.choice([True, False]),
            is_discounted=random.choice([True, False]),
            discount=random.randint(0, 30),
            image=f"img/bike-{fake.uuid4()}",
            created_at=fake.date_time_between(start_date="-2y", end_date="-1y"),
            updated_at=fake.date_time_between(start_date="-1y", end_date="now"),
            deleted_at=None if random.choice([True, False]) else fake.date_time_between(start_date="-6m", end_date="now")
        )
        session.add(bicycle)

    # Generate test data for Transaction
    for _ in range(20):
        transaction = Transaction(
            id=f"Trans-{fake.uuid4()}",
            uid=random.randint(1, 20),
            bid=random.randint(1, 20),
            cid=random.randint(1, 20),
            created_at=fake.date_time_between(start_date="-1y", end_date="now"),
            updated_at=fake.date_time_between(start_date="-1y", end_date="now"),
            start_lat=fake.latitude(),
            start_lng=fake.longitude(),
            end_lat=None if random.choice([True, False]) else fake.latitude(),
            end_lng=None if random.choice([True, False]) else fake.longitude(),
            start_time=fake.date_time_between(start_date="-1y", end_date="now"),
            status=random.choice(["active", "completed", "cancelled", "refunded", "pending"]),
            is_active=random.choice([True, False]),
            is_completed=random.choice([True, False]),
            is_cancelled=random.choice([True, False]),
            is_refunded=random.choice([True, False]),
            is_reviewed=random.choice([True, False]),
            review=fake.text(),
            rating=random.randint(1, 5)
        )
        session.add(transaction)

    # Commit all changes
    session.commit()

# Example of usage
# Assuming `SessionLocal` is your SQLAlchemy session maker
# from app.database.conn import SessionLocal
#
# with SessionLocal() as session:
#     create_test_data(session)
