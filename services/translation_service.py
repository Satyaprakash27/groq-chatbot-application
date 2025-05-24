import os

from helpers.model_helper import ModelHelper
from helpers.output_helper import OutputHelper
from helpers.prompt_helper import PromptHelper

class TranslationService:
    def __init__(self):
        pass

    def run_chain(self, language: str = "English", text: str = "Hello, world!"):
        """
        Runs a chain with the specified language and text.
        
        Args:
            language (str): The language to use for the chain.
            text (str): The text to process.
        
        Returns:
            dict: The output of the chain.
        """
        model_helper = ModelHelper()
        output_helper = OutputHelper()
        prompt_helper = PromptHelper()
        model = model_helper.get_model()
        prompt = prompt_helper.get_prompt(language, text)
        
        response = model.invoke(prompt)
        
        return output_helper.get_output_parser(result=response).content