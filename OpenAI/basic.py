import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Engine.list()

print(response)