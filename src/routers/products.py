from fastapi import APIRouter, responses


router = APIRouter()


@router.get("/")
async def home() -> str:
    "Página de inicio."
    return responses.RedirectResponse(router.docs_url)