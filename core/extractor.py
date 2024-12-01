from models.resume_schema import Resume
from .openai_client import OpenAIClient

class Extractor :
    def __init__(self) -> None:
        self.client = OpenAIClient()
        
    def extract_resume(self, resume_text):
        completion = self.client.execute(
            prompt={
                "system": "Extract the resume information.",
                "user": resume_text
            },
            ResponseModel=Resume
        )
        return completion