from fastapi import FastAPI
import uvicorn
from utils import constants
from utils import users as users_utils


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
    "Retorna la lista de usuarios o un usuario concreto en base al id."
    if id:
        user = users_utils.get_user(id)
        if not user:
            return {"error": constants.ERR_USER_NOT_FOUND}
    return constants.USERS


@app.post("/users/save")
async def save_users(users: list) -> dict:
    "Guarda los usuarios que sean indicados"
    failed_users = []
    success_users = []
    for user in users:
        success, result = users_utils.save_user(user)
        if not success:
            failed_users.append({"user": user, "result": result})
            continue
        success_users.append({"user": user, "result": result})
    result = {"success_users": success_users, "failed_users": failed_users}
    return result


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)
