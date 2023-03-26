import users_model


USERS = [
    users_model.User(
        id=1,
        name="Alejo",
        surname="Sarmiento",
        age=22
    ),
    users_model.User(
        id=2,
        name="Carlos",
        surname="Carloso",
        age=59
    )
]

ERR_USER_NOT_FOUNT = {
    "error": "Usuario no encontrado."
}