from project.logic.equipment import Equipment
from project.logic.classes import get_unit_classes
from project.service.user import UserService
from project.dao.models.user import UserSchema
from project.dao.user import UserDao
from project.setup_db import db

equipment = Equipment()
unit_classes = get_unit_classes()

user_dao = UserDao(session=db.session)
user_service = UserService(user_dao)
user_schema = UserSchema()
