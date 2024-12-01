from pydantic import BaseModel
from openai import OpenAI
from models.resume_schema import Resume
import json

from core.extractor import Extractor

extractor = Extractor()
with open("data/resume.txt", "r") as file:
    data = file.read()
    
resume = extractor.extract_resume(data)