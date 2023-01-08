from pydantic import BaseModel


class User(BaseModel):
    email: str
    login: str
    phone: str
