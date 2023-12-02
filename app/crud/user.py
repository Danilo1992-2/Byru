from datetime import datetime
from sqlalchemy.orm import Session
from models.user import User
import asyncio


async def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


async def create_user(db: Session, name: str, password: str, user: str,
                document: str):
    new_user = User()
    new_user.name = name
    new_user.document = document
    new_user.password = password
    new_user.create_at = datetime.now()
    new_user.user = user
    db.add(new_user)
    db.commit()
    return new_user
