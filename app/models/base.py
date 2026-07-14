"""
Abstract interface for all AI models.

Every production model should implement this interface.
"""

from abc import ABC, abstractmethod

from app.api.schemas.inference import (
    InferenceRequest,
    InferenceResponse,
)


class BaseModel(ABC):
    """
    Base interface for AI models.
    """

    @abstractmethod
    def predict(
        self,
        request: InferenceRequest,
    ) -> InferenceResponse:
        """
        Run model inference.
        """
        raise NotImplementedError