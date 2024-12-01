from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    # Anthropic Config
    OPENAI_API_KEY: str
    OPENAI_MODEL_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()

