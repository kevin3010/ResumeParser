from pydantic import BaseModel
from openai import OpenAI
from .config import settings


class OpenAIClient: 
    
    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
        
    def execute(self, prompt, ResponseModel):
        completion = self.client.beta.chat.completions.parse(
            model=settings.OPENAI_MODEL_NAME,
            messages=[
                {"role": "system", "content": prompt["system"]},
                {"role": "user", "content": prompt["user"]}
            ],
            response_format=ResponseModel,
            temperature=0.5
        )
        
        print(completion)
        
        return completion.choices[0].message.parsed 
        
