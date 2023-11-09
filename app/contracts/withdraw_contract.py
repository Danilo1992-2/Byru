from pydantic import BaseModel


class NewWithdrawContract(BaseModel):
    user_id: int
    description: str
    value: float
