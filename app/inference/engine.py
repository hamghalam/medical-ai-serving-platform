"""
Central inference engine.
"""

from app.inference.pipeline import InferencePipeline


class InferenceEngine:

    def __init__(self):

        self.pipeline = InferencePipeline()

    def run(
        self,
        image,
        question,
        metadata=None,
    ):

        return self.pipeline.run(
            image=image,
            question=question,
            metadata=metadata,
        )