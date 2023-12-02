from sqlalchemy import (Column, Integer, Float, String, Date, ForeignKey)
from sqlalchemy.orm import relationship
from db.base_class import Base


class Withdraw(Base):
    __tablename__: str = "withdraw"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    value: float = Column(Float())
    createat: Date = Column(Date())
    description: str = Column(String(200))
    month: int = Column(Integer())
    user_id: int = Column(Integer(), ForeignKey('user.id'))
    user = relationship('User', back_populates='withdraw', uselist=False)
    id_expense: int = Column(Integer())
