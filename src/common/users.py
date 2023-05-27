from common import constants
from models.users import User
from pydantic import ValidationError

#TODO Docker for db

def validate_user(user, keys=[]):
    try:
        User.validate(User(**user)) if isinstance(user, dict) else User.validate(user)
        return True, None
    except ValidationError as vex:
        fault_keys = [error["loc"][0] for error in vex.errors() if str(error["loc"][0]) in keys] if keys \
            else [error["loc"][0] for error in vex.errors()]
        if fault_keys:
            return False, constants.ERR_SCHEMA.format(err_args=", ".join(fault_keys))
        return True, None


def get_users(id: int = None):
    if id:
        user = next((user for user in constants.USERS if user.id == id), None)
        if not user:
            return False, constants.ERR_USER_NOT_FOUND
        return True, user
    return constants.USERS


def save_user(user):
    success, result = validate_user(user)
    if not success:
        return False, result
    if get_users(user.id)[0]:
        return False, constants.ERR_USER_ALREADY_EXISTS.format(id=user.id)
    constants.USERS.append(user)
    return True, constants.MSG_SUCCESS_SAVE


def update_user(user):
    success, result = validate_user(user, keys=["id"])
    if not success:
        return False, str(result)
    success, current_user = get_users(user["id"])
    if not success:
        return False, constants.ERR_USER_NOT_FOUND
    index = constants.USERS.index(current_user)
    updated_user = current_user.dict()
    updated_user.update(user)
    new_user = User(**updated_user)
    if new_user == current_user:
        return False, constants.ERR_USER_NOT_CHANGED.format()
    constants.USERS[index] = new_user
    return True, constants.USERS[index]


def remove_user(user_id):
    success, current_user = get_users(user_id)
    if not success:
        return False, constants.ERR_USER_NOT_FOUND
    index = constants.USERS.index(current_user)
    constants.USERS.pop(index)
    return True, "Usuario eliminado con éxito"
