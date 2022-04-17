import requests
import os
import json
apiKey = os.environ.get("OPENAI_API_KEY")
headers = {    
  'Content-Type': 'application/json',    
  'Authorization': 'Bearer ' + apiKey}
endpoint = 'https://api.openai.com/v1/engines/davinci/completions'
params = {    
  "prompt": "Translate from English to Uzbek\n---\n\nEnglish: How are you?\nUzbek:",    
  "temperature": 0.5,    
  "max_tokens": 15,    
  "top_p": 1,    
  "frequency_penalty": 0,    
  "presence_penalty": 0,    
  "stop": ["---"]}

result = requests.post(endpoint, headers=headers, data=json.dumps(params))
print(params["prompt"] + result.json()["choices"][0]["text"])
# print(result)
