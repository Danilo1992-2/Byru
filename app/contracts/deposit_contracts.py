from pydantic import BaseModel


class NewDepositContract(BaseModel):
    user_id: int
    description: str
    value: float

class all_values_current_month(BaseModel):
    createat: str
    value: float
