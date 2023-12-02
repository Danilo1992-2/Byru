from datetime import datetime
from sqlalchemy.orm import Session
from models.withdraw import Withdraw
from enums.expenses_enum import ExpenseEnum
import asyncio

async def get_withdraw(db: Session, user_id: int):
    return db.query(Withdraw).filter(Withdraw.user_id == user_id).all()

async def get_withdraw_current_month(user_id: int, db: Session):
    first_day = datetime.now().replace(day=1).date()
    today = datetime.now().date()
    query = db.query(Withdraw).filter(Withdraw.createat.between(first_day, today),
                                        Withdraw.user_id == user_id).all() 
    return query


async def delete_withdraw(db: Session, id_withdraw: int):
    db.query(Withdraw).filter(Withdraw.id == id_withdraw).delete()
    db.commit()

async def  add_withdraw(db: Session, user_id: int, value: float, description: str, expanse: int, date: datetime = datetime.now()):
    new_withdraw = Withdraw()
    new_withdraw.createat =  date if date != None else datetime.now() 
    new_withdraw.month = datetime.now().month
    new_withdraw.description = description
    new_withdraw.user_id = user_id
    new_withdraw.value = value
    new_withdraw.id_expense = expansesReturn(expanse).value
    db.add(new_withdraw)
    db.commit()
    return new_withdraw


def expansesReturn(id: int):
    if id == 1:
        return ExpenseEnum.STUDIO
    elif id == 3:
        return ExpenseEnum.SAUDE
    else:
        return ExpenseEnum.PESSOAL
