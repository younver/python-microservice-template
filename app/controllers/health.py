from fastapi import APIRouter
from app.views import HealthResponse

router = APIRouter()

@router.get("/health-check")
async def health_check() -> HealthResponse:
    return HealthResponse(status="healthy")
