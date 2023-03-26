from fastapi import FastAPI, Request
import constants


app = FastAPI()
# Start server: uvicorn [mmodule_name]:app --reload


@app.get("/")
async def home() -> dict:
    "Página de inicio."
    msg = {
        "msg": "Hola"
    }
    return msg


@app.get("/alive")
async def alive() -> str:
    "Chequea si la aplicación está viva."
    return "¡Estoy vivo!"


# Users methods.


@app.get("/users")
async def get_users() -> list:
    "Retorna todos los usuarios registrados."
    return constants.USERS


@app.get("/user/{id}")
async def get_user(id: int) -> dict:
    "Retorna un usuario en base al id."
    user = list(filter(lambda user: user.id == id, constants.USERS))
    try:
        return user[0]
    except IndexError:
        return {"error": "Usuario no encontrado."}

