from pydantic import BaseModel


class NewWithdrawContract(BaseModel):
    user_id: int
    description: str
    id_expenses: int
    installments: int = None
    value: float
    card: bool = False
    card_turned: bool = False

class all_values_current_month(BaseModel):
    create_at: str
    id_expenses: int
    value: float
