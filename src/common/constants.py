from models import users as model


USERS = [
    model.User(
        id=1,
        name="Alejo",
        surname="Sarmiento",
        age=22
    ),
    model.User(
        id=2,
        name="Carlos",
        surname="Carloso",
        age=59
    )
]

ERR_USER_NOT_FOUND = "Usuario no encontrado."

ERR_USER_ALREADY_EXISTS = "El usuario con id {id} ya existe."

ERR_USER_NOT_CHANGED = "El usuario ingresado posee los mismos datos."

ERR_SCHEMA = "El usuario ingresado no tiene la estructura adecuada. Argumentos faltantes o incorrectos: {err_args}." 

MSG_SUCCESS_GENERIC = "Éxito al realizar la operación."

MSG_SUCCESS_SAVE_USER = "Exito al guardar el usuario."