"""
Input preprocessing.

Future responsibilities:
- Image loading
- Resize
- Normalization
- Metadata parsing
"""


class Preprocessor:

    def run(
        self,
        image,
        question: str,
        metadata=None,
    ):
        """
        Placeholder preprocessing.

        Returns data unchanged.
        """

        return {
            "image": image,
            "question": question,
            "metadata": metadata,
        }