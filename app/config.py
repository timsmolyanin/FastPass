from dotenv import load_dotenv
import os


load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT=os.environ.get("DB_PORT")
DB_NAME=os.environ.get("DB_NAME")
DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")

KDF_SALT_SIZE = 16         # The size of salt in bytes
KDF_ITERATIONS = 100_000   # Count of iterations for KDF
PASSWORDS_STORAGE_PATH = "passwords"