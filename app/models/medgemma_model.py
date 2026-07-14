"""
Production-ready MedGemma model wrapper.

This PR only adds the model wrapper.
Actual inference will be implemented later.
"""

from __future__ import annotations

import logging
from typing import Optional

import torch
from transformers import (
    AutoModelForImageTextToText,
    AutoProcessor,
)

from app.api.schemas.inference import (
    InferenceRequest,
    InferenceResponse,
)
from app.models.base import BaseModel

logger = logging.getLogger(__name__)


class MedGemmaModel(BaseModel):
    """
    Wrapper around Google's MedGemma model.
    """

    def __init__(
        self,
        model_name: str,
        device: Optional[str] = None,
    ) -> None:

        self.model_name = model_name

        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"

        self.device = device

        self.processor: AutoProcessor | None = None
        self.model: AutoModelForImageTextToText | None = None

    def load(self) -> None:
        """
        Lazily load the model.
        """

        if self.model is not None:
            return

        logger.info("Loading model %s", self.model_name)

        self.processor = AutoProcessor.from_pretrained(
            self.model_name
        )

        self.model = AutoModelForImageTextToText.from_pretrained(
            self.model_name,
            torch_dtype=(
                torch.float16
                if self.device == "cuda"
                else torch.float32
            ),
        )

        self.model.to(self.device)
        self.model.eval()

        logger.info("Model loaded successfully.")

    def predict(
        self,
        request: InferenceRequest,
    ) -> InferenceResponse:

        self.load()

        return InferenceResponse(
            answer="MedGemma wrapper is working.",
            confidence=1.0,
            latency_ms=0,
            model_name=self.model_name,
        )