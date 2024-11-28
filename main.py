from pydantic import BaseModel
from openai import OpenAI
from models.resume_schema import Resume
import json
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
# model = "gpt-4o-2024-08-06"
model = "gpt-4o-mini"

with open("data/resume.txt", "r") as file:
    data = file.read()

completion = client.beta.chat.completions.parse(
    model=model,
    messages=[
        {"role": "system", "content": "Extract the resume information."},
        {"role": "user", "content": data},
    ],
    response_format=Resume,
)

resume = completion.choices[0].message.parsed

# Save the extracted resume information to a JSON file
resume_dict = resume.dict()
with open("data/resume_info.json", "w") as file:
    json.dump(resume_dict, file, indent=4)