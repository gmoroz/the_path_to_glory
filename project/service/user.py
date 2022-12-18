from operator import itemgetter
from flask import session
from project.dao.models.user import User
from flask_bcrypt import generate_password_hash, check_password_hash
from project.dao.user import UserDao
from project.helpers import encode_token
from project.constants import WIN


class UserService:
    def __init__(self, dao: UserDao) -> None:
        self.dao = dao

    def get_all(self) -> list[User]:
        return self.dao.get_all()

    def get_user(self, username: str) -> User:
        return self.dao.get_user(username)

    def create(self, user_d: dict) -> None:
        user_d["password"] = generate_password_hash(user_d.get("password")).decode(
            "utf-8"
        )
        self.dao.create(user_d)

    def update_password(self, passwords: dict) -> bool:
        old_password, new_password, new_password_repeated = itemgetter(
            "old_password", "new_password", "new_password_repeated"
        )(passwords)
        if new_password != new_password_repeated:
            return False
        if user_d := encode_token(session.get("token")):
            user = self.get_user(user_d.get("username"))
            if check_password_hash(user.password, old_password):
                user.password = generate_password_hash(new_password)
                self.dao.update(user)
                return True
        return False

    def delete(self, username: str) -> None:
        self.dao.delete(username)

    def update(self, user_d):
        self.dao.update(self.get_user(user_d.get("username")))

    def update_statistics(self, battle_result):
        user_d = encode_token(session["token"])
        user = self.get_user(user_d.get("username"))
        if battle_result == WIN:
            user.wins_count += 1
        else:
            user.loses_count += 1
        self.update({"username": user.username})
