"""
Mock implementation of the AI model.

Used during backend development before integrating
the actual MedGemma model.
"""

import random
import time

from app.api.schemas.inference import (
    InferenceRequest,
    InferenceResponse,
)

from app.models.base import BaseModel


class MockModel(BaseModel):
    """
    Fake model for development.
    """

    def predict(
        self,
        request: InferenceRequest,
    ) -> InferenceResponse:

        start = time.perf_counter()

        #
        # Simulate GPU inference
        #
        time.sleep(0.4)

        latency = int((time.perf_counter() - start) * 1000)

        possible_answers = [

            "No abnormal findings detected.",

            "One lesion is visible.",

            "Two liver lesions are visible.",

            "Further clinical review is recommended.",

        ]

        return InferenceResponse(

            answer=random.choice(possible_answers),

            confidence=round(
                random.uniform(0.82, 0.99),
                2,
            ),

            latency_ms=latency,

            model_name=request.model_name,

        )