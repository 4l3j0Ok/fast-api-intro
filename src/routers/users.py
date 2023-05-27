from fastapi import APIRouter, HTTPException
import common.users as functions
from models.users import User, Success


router = APIRouter()


@router.get("/")
async def get_users(id: int = None) -> User | list[User]:
    "Retorna la lista de usuarios o un usuario concreto en base al id."
    if id:
        success, result = functions.get_users(id)
        if not success:
            raise HTTPException(status_code=406, detail=result)
        return result
    return functions.get_users()


@router.post("/save/")
async def save_user(user: User) -> Success:
    "Guarda el usuario que sea indicado."
    success, result = functions.save_user(user)
    if not success:
        raise HTTPException(status_code=400, detail=result)
    return Success(input=user, detail=result)


@router.put("/update")
async def update_user(user: dict) -> Success:
    "Actualiza el usuario que sea indicado."
    success, result = functions.update_user(user)
    if not success:
        raise HTTPException(status_code=400, detail=result)
    return Success(input=user, detail=result)


@router.delete("/remove")
async def remove_user(id: int) -> Success:
    "Remueve el usuario que sea indicado."
    success, result = functions.remove_user(id)
    if not success:
        raise HTTPException(status_code=400, detail=result)
    return Success(input=id, detail=result)
