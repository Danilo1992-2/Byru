from datetime import datetime
from sqlalchemy.orm import Session
from models.withdraw import Withdraw


def get_withdraw(db: Session, user_id: int):
    return db.query(Withdraw).filter(Withdraw.user_id == user_id).all()


def add_withdraw(db: Session, user_id: int, value: float, description: str):
    new_withdraw = Withdraw()
    new_withdraw.createat = datetime.now()
    new_withdraw.month = datetime.now().month
    new_withdraw.description = description
    new_withdraw.user_id = user_id
    new_withdraw.value = value
    db.add(new_withdraw)
    db.commit()
    return new_withdraw
