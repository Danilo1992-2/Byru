from datetime import datetime
from sqlalchemy.orm import Session
from models.withdraw import Withdraw
from sqlalchemy import func

def get_withdraw(db: Session, user_id: int):
    return db.query(Withdraw).filter(Withdraw.user_id == user_id).all()

def get_withdraw_current_month(user_id: int, db: Session):
    first_day = datetime.now().replace(day=1).date()
    today = datetime.now().date()
    query = db.query(Withdraw).filter(Withdraw.createat.between(first_day, today),
                                        Withdraw.user_id == user_id).all() 
    return query

def delete_withdraw(db: Session, id_withdraw: int):
    db.query(Withdraw).filter(Withdraw.id == id_withdraw).delete()
    db.commit()


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
