"""
Inference API schemas.

These Pydantic models define the request and response
contracts exposed by the REST API.
"""

from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------
# Patient Metadata
# ---------------------------------------------------------


class PatientMetadata(BaseModel):
    """
    Optional patient metadata supplied alongside the image.

    This information can later be injected into prompts
    or used for clinical reasoning.
    """

    age: int | None = Field(
        default=None,
        ge=0,
        le=120,
        description="Patient age",
    )

    sex: str | None = Field(
        default=None,
        description="Patient sex",
        examples=["male", "female"],
    )

    modality: str | None = Field(
        default=None,
        description="Imaging modality",
        examples=["X-ray", "CT", "MRI"],
    )

    study_description: str | None = Field(
        default=None,
        description="Study description",
    )

    additional_info: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata",
    )


# ---------------------------------------------------------
# Inference Request
# ---------------------------------------------------------


class InferenceRequest(BaseModel):
    """
    Input payload for model inference.

    Image upload will be added in a future PR.
    """

    question: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="Clinical question",
        examples=[
            "How many liver lesions are visible?"
        ],
    )

    metadata: PatientMetadata = Field(
        default_factory=PatientMetadata,
    )

    model_name: str = Field(
        default="mock-medgemma",
        description="Model identifier",
    )


# ---------------------------------------------------------
# Inference Response
# ---------------------------------------------------------


class InferenceResponse(BaseModel):
    """
    Standard API response.
    """

    answer: str

    confidence: float

    latency_ms: int

    model_name: str