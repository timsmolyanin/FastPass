
from fastapi import APIRouter, Depends, HTTPException
from schemas import Password
import crud

router = APIRouter()

@router.post("/passwords")
def create_password(password: Password, master_password: str, username: str):
    """
    Создает новый пароль, шифруя его с использованием мастер-пароля.
    """
    result = crud.save_encrypted_password(username, password, master_password)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.get("/passwords/{service}")
def get_password(service: str, master_password: str, username: str):
    """
    Возвращает расшифрованный пароль для указанного сервиса.
    """
    result = crud.load_encrypted_password(username, service, master_password)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
