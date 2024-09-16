
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt_data(key: bytes, plaintext: bytes) -> bytes:
    """
    Encrypt user data using set key.
    """
    iv = os.urandom(16)  # Инициализационный вектор
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return iv + ciphertext  # Сохраняем iv вместе с шифротекстом

def decrypt_data(key: bytes, ciphertext: bytes) -> bytes:
    """
    Decrypt user data using set key.
    """
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()
    return plaintext