from datetime import datetime
from sqlalchemy.orm import Session
from models.deposit import Deposit
from sqlalchemy import func


def get_deposits(db: Session, user_id: int):
    query = db.query(Deposit).filter(Deposit.user_id == user_id).all()
    return query

def get_deposits_current_month(db: Session):
    today = datetime.now().strftime('%Y-%m-%d')
    return db.query(Deposit).filter(func.date(Deposit.createat) == today).all()

def add_deposit(db: Session, user_id: int, value: float, description: str):
    new_deposit = Deposit()
    new_deposit.createat = datetime.now()
    new_deposit.month = datetime.now().month
    new_deposit.description = description
    new_deposit.user_id = user_id
    new_deposit.value = value
    db.add(new_deposit)
    db.commit()
    return new_deposit
