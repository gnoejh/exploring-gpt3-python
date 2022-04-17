import requests
import os
import json
apiKey = os.environ.get("OPENAI_API_KEY")
headers = {    
  'Content-Type': 'application/json',    
  'Authorization': 'Bearer ' + apiKey}
endpoint = 'https://api.openai.com/v1/engines/davinci/completions'
params = {    
  "prompt": "Write a description for the following webinar:\n\nDate: Monday, June 5, 2021\nTime: 10 AM PT\nTitle: An introduction to mindfulness\nPresenter: Gabi Calm\n\nEvent Description:",   
  "temperature": 0.5,    
  "max_tokens": 100,    
  "top_p": 1,    
  "frequency_penalty": 0.5,    
  "presence_penalty": 0.5,    
  "stop": ["###"]}
result = requests.post(endpoint, headers=headers, data=json.dumps(params))
print(params["prompt"] + result.json()["choices"][0]["text"])
# print(result)
