from models import users, products


USERS = [
    users.User(
        id=1,
        name="Alejo",
        surname="Sarmiento",
        age=22
    ),
    users.User(
        id=2,
        name="Carlos",
        surname="Carloso",
        age=59
    )
]

PRODUCTS = [
    products.Product(
        id=1,
        name="Fideos",
        price=200
    ),
    products.Product(
        id=2,
        name="Arroz",
        price=250
    )
]

ERR_USER_NOT_FOUND = "Usuario no encontrado."
ERR_USER_ALREADY_EXISTS = "El usuario con id {id} ya existe."
ERR_USER_NOT_CHANGED = "El usuario ingresado posee los mismos datos."

ERR_PRODUCT_NOT_FOUND = "Producto no encontrado."
ERR_PRODUCT_ALREADY_EXISTS = "El producto con id {id} ya existe."
ERR_PRODUCT_NOT_CHANGED = "El producto ingresado posee los mismos datos."

ERR_SCHEMA = "Los datos ingresados no tienen la estructura adecuada. Argumentos faltantes o incorrectos: {err_args}." 
MSG_SUCCESS_GENERIC = "Éxito al realizar la operación."
MSG_SUCCESS_SAVE = "Exito al guardar los datos."