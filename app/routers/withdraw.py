from fastapi import APIRouter, Depends, HTTPException
from db.sessions import get_db
from sqlalchemy.orm import Session
from contracts.withdraw_contract import NewWithdrawContract,all_values_current_month
from crud.withdraw import get_withdraw, add_withdraw, get_withdraw_current_month, delete_withdraw


router = APIRouter()


@router.get("/{user_id}")
async def read_all_deposit(user_id: int, db: Session = Depends(get_db)):
    deposits = get_withdraw(db, user_id)

    if deposits is None:
        raise HTTPException(status_code=404, detail="Dados não encontrados.")
    return deposits

@router.get('/all-withdrawals-current-moth/{user_id}')
async def get_total_value_current_month(user_id: int, db: Session = Depends(get_db)):
    query = get_withdraw_current_month(user_id, db)

    if query is None:
        raise HTTPException(status_code=404, detail="Registro não encontrado.")
    return query

@router.delete('/{id}')
async def delete_withdrawal(id: int, db: Session = Depends(get_db)):
    delete_withdraw(db, id)
    return "Ok"

@router.post("/add-withdrawal", response_model=NewWithdrawContract)
async def add_new_withdraw(withdraw_data: NewWithdrawContract,
                           db: Session = Depends(get_db)):
    new_deposit = add_withdraw(db, withdraw_data.user_id, withdraw_data.value,
                               withdraw_data.description)
    return new_deposit
