import requests
import json
import os

textInput = "What religion are you?"
prompts = []
wordArray = textInput.split()
for word in wordArray:
  prompts.append("<|endoftext|>" + word + "\n--\nLabel:")
  
payload = json.dumps({
  "prompt": prompts,
  "max_tokens": 1,
  "temperature": 0.0,
  "top_p": 0
})
url = "https://api.openai.com/v1/engines/content-filter-alpha/completions?OPEN_API_KEYS=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"

headers = {
    'Authorization':
    'Bearer ' + os.environ.get("OPENAI_API_KEY"),
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

for word in response.json()['choices']:
  print(wordArray[word['index']] + ' : ' + word['text'])
