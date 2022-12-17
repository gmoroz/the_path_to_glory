import os
from dotenv import load_dotenv

load_dotenv()

HEADERS = {"Content-Type": "text/html"}
TOKEN_EXPIRE_MINUTES = 30
TOKEN_EXPIRE_DAYS = 15
JWT_ALGORITHM = os.environ["JWT_ALGORITHM"]
JWT_SECRET = os.environ["JWT_SECRET"]

WIN = "Игрок выиграл битву"
LOSE = "Игрок проиграл битву"
DRAW = "Ничья"
