"""
Model registry.

Provides a central location for registering and retrieving
AI models.
"""

from typing import Dict

from app.models.base import BaseModel
from app.models.mock_model import MockModel


class ModelRegistry:
    """
    Registry for available AI models.
    """

    def __init__(self) -> None:

        self._models: Dict[str, BaseModel] = {}

        self.register(
            "mock-medgemma",
            MockModel(),
        )

    def register(
        self,
        name: str,
        model: BaseModel,
    ) -> None:
        """
        Register a model instance.
        """

        self._models[name] = model

    def get(
        self,
        name: str,
    ) -> BaseModel:
        """
        Retrieve a registered model.
        """

        if name not in self._models:
            raise ValueError(
                f"Unknown model '{name}'"
            )

        return self._models[name]

    def list_models(
        self,
    ) -> list[str]:
        """
        List registered models.
        """

        return sorted(self._models.keys())


registry = ModelRegistry()