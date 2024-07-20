
from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
load_dotenv()

api_key=os.getenv("openai_api_key")

llm = OpenAI(openai_api_key=api_key)

response=llm("Who is currently President of United States of America?")
print(response)
