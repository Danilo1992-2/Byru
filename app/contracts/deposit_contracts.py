from pydantic import BaseModel


class NewDepositContract(BaseModel):
    user_id: int
    description: str
    value: float
