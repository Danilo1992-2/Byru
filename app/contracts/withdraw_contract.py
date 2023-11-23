from pydantic import BaseModel


class NewWithdrawContract(BaseModel):
    user_id: int
    description: str
    value: float

class all_values_current_month(BaseModel):
    create_at: str
    value: float
