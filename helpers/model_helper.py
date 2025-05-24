import os

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import SecretStr
load_dotenv()

class ModelHelper:
    def __init__(self):
        """
        Initializes the ModelHelper class.
        This class is responsible for managing the Groq model instance.
        """
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        if not self.groq_api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set.")
        self.model = ChatGroq(
            model="Gemma2-9b-It",
            api_key=SecretStr(self.groq_api_key)
        )
    
    def get_model(self):
        """
        Returns the Groq model instance.
        
        Returns:
            ChatGroq: The Groq model instance.
        """
        return self.model