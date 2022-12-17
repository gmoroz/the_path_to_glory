import os
from dotenv import load_dotenv

load_dotenv()

HEADERS = {"Content-Type": "text/html"}
SALT = os.environ["SALT"]
