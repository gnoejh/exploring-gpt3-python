import requests
import os
import json
apiKey = os.environ.get("OPENAI_API_KEY")
headers = {    
  'Content-Type': 'application/json',    
  'Authorization': 'Bearer ' + apiKey}
endpoint = 'https://api.openai.com/v1/engines/davinci/completions'
params = {    
  "prompt": "Provide the meaning for the following acronym.\n---\n\nacronym: LOL\nmeaning: Laugh out loud\nacronym: BRB\nmeaning: Be right back\nacronym: L8R",    
  "temperature": 0.5,    
  "max_tokens": 15,    
  "top_p": 1,    
  "frequency_penalty": 0,    
  "presence_penalty": 0,
  "stop": ["acronym"]
}

# params = {    
#   "prompt": "Generate acronyms.\n---\n\nmeaning: Laugh out loud \nacronym: LOL\nmeaning: I am happy",    
#   "temperature": 0.5,    
#   "max_tokens": 50,    
#   "top_p": 1,    
#   "frequency_penalty": 0,    
#   "presence_penalty": 0,
#   "stop": ["meaning"]
# }
          
result = requests.post(endpoint, headers=headers, data=json.dumps(params))
print(params["prompt"] + result.json()["choices"][0]["text"])
# print(result)
