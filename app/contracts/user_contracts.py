from pydantic import BaseModel


class NewUserContract(BaseModel):
    name: str
    document: str
    user: str
    password: str
