from fastapi import FastAPI
import uvicorn
from utils import constants
from utils import users as users_utils
from models.users_model import User


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
async def get_users(id: int = None) -> list[User] | User:
    "Retorna la lista de usuarios o un usuario concreto en base al id."
    if id:
        user = users_utils.get_user(id)
        if not user:
            return {"error": constants.ERR_USER_NOT_FOUND}
        return user
    return constants.USERS


@app.post("/users/save")
async def save_users(users: list[dict]) -> dict:
    "Guarda los usuarios que sean indicados"
    failed_users = []
    success_users = []
    for user in users:
        success, result = users_utils.save_user(user)
        if not success:
            failed_users.append({"input": user, "result": result})
            continue
        success_users.append({"input": user, "result": result})
    result = {"success_users": success_users, "failed_users": failed_users}
    return result


@app.put("/users/update")
async def update_users(users: list[dict]) -> dict:
    not_updated_users = []
    updated_users = []
    for user in users:
        success, result = users_utils.update_user(user)
        if not success:
            not_updated_users.append({"input": user, "reason": result})
            continue
        updated_users.append(result)
    result = {"updated_users": updated_users, "not_updated_users": not_updated_users}
    return result


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
