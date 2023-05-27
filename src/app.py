from fastapi import FastAPI, responses, HTTPException
import uvicorn
from utils import users as users_utils
from models.users_model import User, Success


app = FastAPI()
# Start server: uvicorn [mmodule_name]:app --reload


@app.get("/")
async def home() -> str:
    "Página de inicio."
    return responses.RedirectResponse(app.docs_url)


@app.get("/alive")
async def alive() -> str:
    "Chequea si la aplicación está viva."
    return "Estoy vivo!"


# Users methods.


@app.get("/users")
async def get_users(id: int = None) -> User | list[User]:
    "Retorna la lista de usuarios o un usuario concreto en base al id."
    if id:
        success, result = users_utils.get_users(id)
        if not success:
            raise HTTPException(status_code=406, detail=result)
        return result
    return users_utils.get_users()


@app.post("/users/save/")
async def save_user(user: User) -> Success:
    "Guarda el usuario que sea indicado."
    success, result = users_utils.save_user(user)
    if not success:
        raise HTTPException(status_code=400, detail=result)
    return Success(input=user, detail=result)


@app.put("/users/update")
async def update_user(user: dict) -> Success:
    "Actualiza el usuario que sea indicado."
    success, result = users_utils.update_user(user)
    if not success:
        raise HTTPException(status_code=400, detail=result)
    return Success(input=user, detail=result)


@app.delete("/users/remove")
async def remove_user(id: int) -> Success:
    "Remueve el usuario que sea indicado."
    success, result = users_utils.remove_user(id)
    if not success:
        raise HTTPException(status_code=400, detail=result)
    return Success(input=id, detail=result)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
