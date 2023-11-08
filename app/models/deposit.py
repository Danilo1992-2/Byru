from sqlalchemy import (Column, Integer, Float, Date, ForeignKey)
from sqlalchemy.orm import relationship
from db.base_class import Base


class Deposit(Base):
    __tablename__: str = "deposit"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    value: float = Column(Float())
    createat: Date = Column(Date())
    month: int = Column(Integer())
    user_id: int = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='deposit', uselist=False)
