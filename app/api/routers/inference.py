"""
Inference API endpoints.
"""

from fastapi import APIRouter, Depends

from app.api.schemas.inference import (
    InferenceRequest,
    InferenceResponse,
)

from app.services.inference_service import InferenceService


router = APIRouter(
    prefix="/v1/inference",
    tags=["Inference"],
)


def get_inference_service() -> InferenceService:
    """
    Dependency provider.

    Later this will inject Model Registry,
    Redis, PostgreSQL, etc.
    """

    return InferenceService()


@router.post(
    "",
    response_model=InferenceResponse,
)
async def run_inference(
    request: InferenceRequest,
    service: InferenceService = Depends(
        get_inference_service
    ),
) -> InferenceResponse:
    """
    Run model inference.
    """

    return service.predict(request)