"""
Inference service.

Business logic layer.
"""

from app.api.schemas.inference import (
    InferenceRequest,
    InferenceResponse,
)

from app.core.registry import registry
from app.inference.engine import InferenceEngine


class InferenceService:
    """
    Business logic for inference.
    """

    def __init__(self) -> None:

        self.engine = InferenceEngine()

    def predict(
        self,
        request: InferenceRequest,
    ) -> InferenceResponse:

        #
        # Get requested model
        #

        model = registry.get(
            request.model_name
        )

        #
        # Run pipeline
        #

        self.engine.run(
            image=None,
            question=request.question,
            metadata=None,
        )

        #
        # Execute model
        #

        return model.predict(request)