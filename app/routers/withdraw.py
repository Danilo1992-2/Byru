from fastapi import APIRouter, Depends, HTTPException
from db.sessions import get_db
from sqlalchemy.orm import Session
from contracts.withdraw_contract import NewWithdrawContract
from crud.withdraw import get_withdraw, add_withdraw


router = APIRouter()


@router.get("/deposit/{user_id}")
async def read_all_deposit(user_id: int, db: Session = Depends(get_db)):
    deposits = get_withdraw(db, user_id)

    if deposits is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deposits


@router.post("/deposit/add-deposit", response_model=NewWithdrawContract)
async def add_new_withdraw(withdraw_data: NewWithdrawContract,
                           db: Session = Depends(get_db)):
    new_deposit = add_withdraw(db, withdraw_data.user_id, withdraw_data.value,
                               withdraw_data.description)

    return new_deposit
