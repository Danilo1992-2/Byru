from sqlalchemy import (Column, Integer, String, Date)
from sqlalchemy.orm import relationship
from db.base_class import Base


class User(Base):
    __tablename__: str = "user"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(50))
    document: str = Column(String(11))
    user: str = Column(String(50))
    create_at: Date = Column(Date())
    password: str = Column(String(50))
    deposit = relationship('Deposit', back_populates='user', uselist=False)
    withdraw = relationship('Withdraw', back_populates='user')
