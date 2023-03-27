from utils import constants
from models.users_model import User
from pydantic import ValidationError


def validate_user(user):
    try:
        User.parse_obj(user)
        return True, None
    except ValidationError as vex:
        return False, vex.errors()


def get_user(id: int):
    user = next((user for user in constants.USERS if user.id == id), None)
    return user

def save_user(user):
    success, errors = validate_user(user)
    if not success:
        return False, constants.ERR_SCHEMA.format(err_args=", ".join(error["loc"][0] for error in errors))
    if get_user(user.get("id")):
        return False, constants.ERR_USER_ALREADY_EXISTS
    constants.users.append(User(**user))
    return True, constants.MSG_SUCCESS_SAVE_USER