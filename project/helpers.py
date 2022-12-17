import base64
import hashlib
import hmac
from project.constants import SALT


def get_hashed_password(password):
    return base64.b64encode(
        hashlib.pbkdf2_hmac("sha256", password.encode(), SALT, 1000)
    )


def check_password(password: str, hashed_password: str) -> bool:
    return hmac.compare_digest(
        base64.b64decode(hashed_password),
        hashlib.pbkdf2_hmac("sha256", password.encode(), SALT, 1000),
    )
