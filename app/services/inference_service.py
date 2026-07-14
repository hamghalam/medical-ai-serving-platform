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
# from app.models.mock_model import MockModel
from app.core.registry import registry


class InferenceService:

    def predict(
        self,
        request: InferenceRequest,
    ) -> InferenceResponse:

        model = registry.get(
            request.model_name
        )

        return model.predict(request)