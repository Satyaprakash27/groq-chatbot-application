import os
from langchain_core.prompts import ChatPromptTemplate


class PromptHelper:
    def __init__(self):
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "Translate the following text to {language}. Give as literal translation as possible and no extra information:"),
                ("human", "{input}"),
            ]
        )

    def get_prompt(self, input_text: str, language: str) -> str:
        """
        Formats and returns a prompt by combining input text and language.

        Args:
            input_text (str): The input text to be included in the prompt.
            language (str): The language specification to be included in the prompt.

        Returns:
            str: A formatted prompt string that incorporates both the input text and language.
        """
        return self.prompt.format(input=input_text, language=language)