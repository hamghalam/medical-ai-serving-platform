"""
Model management endpoints.
"""

from fastapi import APIRouter

from app.core.registry import registry

router = APIRouter(
    prefix="/v1/models",
    tags=["Models"],
)


@router.get("")
async def list_models():
    """
    Return all available models.
    """

    return {
        "models": registry.list_models()
    }