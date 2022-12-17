import os
from dotenv import load_dotenv

load_dotenv()

HEADERS = {"Content-Type": "text/html"}
SALT = os.environ["SALT"]
TOKEN_EXPIRE_MINUTES = os.environ["TOKEN_EXPIRE_MINUTES"]
TOKEN_EXPIRE_DAYS = os.environ["TOKEN_EXPIRE_DAYS"]
JWT_ALGORITHM = os.environ["JWT_ALGORITHM"]
JWT_SECRET = os.environ["JWT_SECRET"]
