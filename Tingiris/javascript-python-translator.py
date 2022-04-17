import requests
import os
import json
apiKey = os.environ.get("OPENAI_API_KEY")
headers = {    
  'Content-Type': 'application/json',    
  'Authorization': 'Bearer ' + apiKey}
endpoint = 'https://api.openai.com/v1/engines/davinci/completions'
params = {    
  "prompt": "Translate from JavaScript to Python\n---\n\nJavaScript:\nconst request = require(\"requests\");\nrequest.get(\"https://example.com\");\n\nPython:\n",    
  "temperature": 0.3,    
  "max_tokens": 15,    
  "top_p": 1,   
  "frequency_penalty": 0,   
  "presence_penalty": 0,   
  "stop": ["---"]
}

result = requests.post(endpoint, headers=headers, data=json.dumps(params))
print(params["prompt"] + result.json()["choices"][0]["text"])
# print(result)
