from fastapi import APIRouter, HTTPException
import common.products as functions
from models.products import Product, Success


router = APIRouter()


@router.get("/")
async def get_products(id: int = None) -> Product | list[Product]:
    "Retorna la lista de usuarios o un usuario concreto en base al id."
    if id:
        success, result = functions.get_products(id)
        if not success:
            raise HTTPException(status_code=406, detail=result)
        return result
    return functions.get_products()


@router.post("/save/")
async def save_product(product: Product) -> Success:
    "Guarda el usuario que sea indicado."
    success, result = functions.save_product(product)
    if not success:
        raise HTTPException(status_code=400, detail=result)
    return Success(input=product, detail=result)


@router.put("/update")
async def update_product(product: dict) -> Success:
    "Actualiza el usuario que sea indicado."
    success, result = functions.update_product(product)
    if not success:
        raise HTTPException(status_code=400, detail=result)
    return Success(input=product, detail=result)


@router.delete("/remove")
async def remove_product(id: int) -> Success:
    "Remueve el usuario que sea indicado."
    success, result = functions.remove_product(id)
    if not success:
        raise HTTPException(status_code=400, detail=result)
    return Success(input=id, detail=result)
