"""
Inference service.

This layer contains the business logic of the application.

Routers should never communicate directly with AI models.
"""

from app.api.schemas.inference import (
    InferenceRequest,
    InferenceResponse,
)

from app.models.base import BaseModel
from app.models.mock_model import MockModel


class InferenceService:
    """
    Service responsible for running AI inference.
    """

    def __init__(
        self,
        model: BaseModel | None = None,
    ) -> None:

        # Default model
        self.model = model or MockModel()

    def predict(
        self,
        request: InferenceRequest,
    ) -> InferenceResponse:
        """
        Execute model inference.
        """

        return self.model.predict(request)