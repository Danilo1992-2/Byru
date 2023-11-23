from fastapi import APIRouter, Depends, HTTPException
from db.sessions import get_db
from contracts.user_contracts import NewUserContract
from models.user import User
from sqlalchemy.orm import Session
from crud.user import get_user, create_user


router = APIRouter()


@router.get("/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/add-user", response_model=NewUserContract)
async def add_user(user_data: NewUserContract, db: Session = Depends(get_db)):
    new_user = User()
    new_user.name = user_data.name
    new_user.document = user_data.document
    new_user.user = user_data.user
    new_user.password = user_data.password

    return create_user(db, user_data.name, user_data.password,
                       user_data.user,
                       user_data.document)
