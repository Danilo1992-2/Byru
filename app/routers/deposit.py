from fastapi import APIRouter, Depends, HTTPException
from db.sessions import get_db
from sqlalchemy.orm import Session
from contracts.deposit_contracts import NewDepositContract
from crud.deposit import get_deposits, add_deposit


router = APIRouter()


@router.get("/deposit/{user_id}")
async def read_all_deposit(user_id: int, db: Session = Depends(get_db)):
    deposits = get_deposits(db, user_id)

    if deposits is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deposits


@router.post("/deposit/add-deposit", response_model=NewDepositContract)
async def add_new_deposit(deposit_data: NewDepositContract,
                          db: Session = Depends(get_db)):
    new_deposit = add_deposit(db, deposit_data.user_id, deposit_data.value,
                              deposit_data.description)

    return new_deposit
