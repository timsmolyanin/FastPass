
from pydantic import BaseModel


class Password(BaseModel):
    service: str
    username: str
    password: str