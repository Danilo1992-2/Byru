from fastapi import APIRouter, Depends, HTTPException
from db.sessions import get_db
from sqlalchemy.orm import Session
from crud.user import get_user


router = APIRouter()


@router.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
