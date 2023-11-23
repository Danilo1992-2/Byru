from fastapi import APIRouter, Depends, HTTPException
from db.sessions import get_db
from sqlalchemy.orm import Session
from contracts.withdraw_contract import NewWithdrawContract,all_values_current_month
from crud.withdraw import get_withdraw, add_withdraw, get_withdraw_current_month


router = APIRouter()


@router.get("/{user_id}")
async def read_all_deposit(user_id: int, db: Session = Depends(get_db)):
    deposits = get_withdraw(db, user_id)

    if deposits is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deposits

@router.get('/all-deposits-current-moth')
async def get_total_value_current_month(db: Session = Depends(get_db)):
     return get_withdraw_current_month(db)

@router.post("/add-deposit", response_model=NewWithdrawContract)
async def add_new_withdraw(withdraw_data: NewWithdrawContract,
                           db: Session = Depends(get_db)):
    new_deposit = add_withdraw(db, withdraw_data.user_id, withdraw_data.value,
                               withdraw_data.description)

    return new_deposit
