
from pydantic import BaseModel


class Password(BaseModel):
    service: str
    username: str
    password: str


class UserCreate(BaseModel):
    username: str
    master_password: str

class UserLogin(BaseModel):
    username: str
    master_password: str