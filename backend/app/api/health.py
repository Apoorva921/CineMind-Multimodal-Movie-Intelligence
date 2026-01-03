from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    return {
        "service": "CineMind API",
        "status": "running"
    }
