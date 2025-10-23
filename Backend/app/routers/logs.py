from fastapi import APIRouter

router = APIRouter(prefix="/logs", tags=["Users"])

@router.get("/create")
def setLogs():
    return [{"id": 1, "name": "John Doe"}]
