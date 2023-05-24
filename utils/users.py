from utils import constants
from models.users_model import User
from pydantic import ValidationError


def validate_user(user, keys=[]):
    try:
        User.validate(User(**user))
        return True, None
    except ValidationError as vex:
        fault_keys = [error["loc"][0] for error in vex.errors() if str(error["loc"][0]) in keys] if keys \
            else [error["loc"][0] for error in vex.errors()]
        if fault_keys:
            return False, constants.ERR_SCHEMA.format(err_args=", ".join(fault_keys))
        return True, None


def get_user(id: int):
    user = next((user for user in constants.USERS if user.id == id), None)
    return user


def save_user(user):
    success, result = validate_user(user)
    if not success:
        return False, result
    if get_user(user["id"]):
        return False, constants.ERR_USER_ALREADY_EXISTS.format(id=user["id"])
    constants.USERS.append(User(**user))
    return True, constants.MSG_SUCCESS_SAVE_USER


def update_user(user):
    success, result = validate_user(user, keys=["id"])
    if not success:
        return False, str(result)
    current_user = get_user(user["id"])
    if not current_user:
        return False, constants.ERR_USER_NOT_FOUND
    index = constants.USERS.index(current_user)
    update_user = current_user.dict()
    update_user.update(user)
    new_user = User(**update_user)
    if new_user == current_user:
        return False, constants.ERR_USER_NOT_CHANGED.format()
    constants.USERS[index] = new_user
    return True, constants.USERS[index]
