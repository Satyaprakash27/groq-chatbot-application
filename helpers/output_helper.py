import os
from typing import Any, Dict, Optional
from langchain_core.output_parsers import StrOutputParser

class OutputHelper:
    def __init__(self):
        """
        Initializes the OutputHelper class.
        This class is responsible for parsing outputs from Langchain runnable interfaces.
        """
        pass

    @staticmethod
    def get_output_parser(result):
        """
        Parses the output from a Langchain runnable interface.

        Args:
            output (Any): The output to be parsed, typically a string or a dictionary.

        Returns:
            Optional[str]: The parsed output as a string, or None if parsing fails.
        """
        try:
            return StrOutputParser().parse(result)
        except Exception as e:
            print(f"Error parsing output: {e}")
            return None