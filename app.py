from fastapi import FastAPI
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
async def get_users(id: int = None) -> dict | list:
    "Retorna un usuario en base al id."
    if id:
        user = next((user for user in constants.USERS if user.id == id), constants.ERR_USER_NOT_FOUNT)
        return user
    return constants.USERS
