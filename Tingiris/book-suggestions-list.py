import requests
import os
import json
apiKey = os.environ.get("OPENAI_API_KEY")
headers = {    
  'Content-Type': 'application/json',    
  'Authorization': 'Bearer ' + apiKey}
endpoint = 'https://api.openai.com/v1/engines/davinci/completions'
params = {    
  "prompt": "Suggest a list of books that everyone should try to read in their lifetime.\n\nBooks:\n1.",   
  "temperature": 0.5,    
  "max_tokens": 100,    
  "top_p": 1,    
  "frequency_penalty": 0.5,    
  "presence_penalty": 0.5,    
  "stop": ["###"]}
result = requests.post(endpoint, headers=headers, data=json.dumps(params))
print(params["prompt"] + result.json()["choices"][0]["text"])
# print(result)
