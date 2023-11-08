from sqlalchemy import (Column, Integer, Float, Date, ForeignKey)
from sqlalchemy.orm import relationship
from db.base_class import Base


class Withdraw(Base):
    __tablename__: str = "withdraw"
    id: str = Column(Integer, primary_key=True, autoincrement=True)
    value: float = Column(Float())
    createat: Date = Column(Date())
    month: int = Column(Integer())
    user_id: int = Column(Integer(), ForeignKey('user.id'))
    user = relationship('User', back_populates='withdraw', uselist=False)
