
from fastapi import APIRouter
from schemas import Password


router = APIRouter()

pass_db = [] # temp vault


@router.get("/passwords")
def get_passwords():
    return {"message": pass_db}

@router.post("/passwords")
def create_password(password: Password):
    pass_db.append(password)
    return {"message": "Password created succesfully!"}
