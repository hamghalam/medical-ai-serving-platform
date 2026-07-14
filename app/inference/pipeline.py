"""
Inference pipeline.
"""

from app.inference.preprocess import Preprocessor
from app.inference.postprocess import Postprocessor


class InferencePipeline:

    def __init__(self):

        self.preprocessor = Preprocessor()

        self.postprocessor = Postprocessor()

    def run(
        self,
        image,
        question,
        metadata=None,
    ):

        inputs = self.preprocessor.run(
            image=image,
            question=question,
            metadata=metadata,
        )

        #
        # Model execution will be added later.
        #

        outputs = inputs

        outputs = self.postprocessor.run(
            outputs,
        )

        return outputs