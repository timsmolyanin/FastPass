

import os
from schemas import Password
from services import key_management, encryption_service
from config import PASSWORDS_STORAGE_PATH


def save_encrypted_password(username: str, password: Password, master_password: str):
    """
    Шифрует и сохраняет пароль в файл.
    """
    salt = key_management.generate_salt()
    key = key_management.derive_key(master_password, salt)
    plaintext = password.password.encode()
    ciphertext = encryption_service.encrypt_data(key, plaintext)

    # Сохраняем соль и шифротекст в файл
    file_path = os.path.join(PASSWORDS_STORAGE_PATH, f"{password.service}_{username}.bin")
    with open(file_path, "wb") as f:
        f.write(salt + ciphertext)
    return {"message": f"Password for {password.service} added successfully!"}

def load_encrypted_password(username: str, service: str, master_password: str):
    """
    Загружает и расшифровывает пароль из файла.
    """
    file_path = os.path.join(PASSWORDS_STORAGE_PATH, f"{service}_{username}.bin")
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        salt = data[:16]
        ciphertext = data[16:]
        key = key_management.derive_key(master_password, salt)
        plaintext = encryption_service.decrypt_data(key, ciphertext)
        return {"service": service, "username": username, "password": plaintext.decode()}
    except FileNotFoundError:
        return {"error": "Password not found"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
