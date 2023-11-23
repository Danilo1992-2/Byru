from fastapi import APIRouter, Depends, HTTPException
from db.sessions import get_db
from sqlalchemy.orm import Session
from contracts.deposit_contracts import NewDepositContract
from crud.deposit import get_deposits, add_deposit, get_deposits_current_month


router = APIRouter()


@router.get("/{user_id}")
async def read_all_deposit(user_id: int, db: Session = Depends(get_db)):
    deposits = get_deposits(db, user_id)

    if deposits is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deposits

@router.get("/all-deposits-current-moth/{user_id}")
async def get_total_value_current_month(user_id: int, db: Session = Depends(get_db)):
    data = get_deposits_current_month(user_id, db)
    return data

@router.post("/add-deposit", response_model=NewDepositContract)
async def add_new_deposit(deposit_data: NewDepositContract,
                          db: Session = Depends(get_db)):
    new_deposit = add_deposit(db, deposit_data.user_id, deposit_data.value,
                              deposit_data.description)

    return new_deposit
