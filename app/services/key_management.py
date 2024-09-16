
import os
from hashlib import pbkdf2_hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from config import KDF_SALT_SIZE, KDF_ITERATIONS


def derive_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=KDF_ITERATIONS,
    )
    key = kdf.derive(master_password.encode())
    return key

def generate_salt() -> bytes:
    """
    Generate random salt for KDF.
    """
    return os.urandom(KDF_SALT_SIZE)