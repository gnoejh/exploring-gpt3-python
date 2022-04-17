import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Correct this to standard English:\n\nShe no went to the market.",
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)