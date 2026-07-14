from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health():
    """
    Health endpoint.
    """

    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "version": settings.VERSION,
    }