from fastapi import APIRouter

router = APIRouter()

@router.post("/me")
async def me(name: str):
    return {
        "Message":  "".join("Welcome " + name)
    }
