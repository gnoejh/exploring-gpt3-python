import requests
import json
import os

url = "https://api.openai.com/v1/engines/content-filter-alpha/completions?OPEN_API_KEYS=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"

payload = json.dumps({
    "prompt": "<|endoftext|>Are you religious?\n--nLabel:",
    "max_tokens": 1,
    "temperature": 0,
    "top_p": 0
})
headers = {
    'Authorization':
    'Bearer ' + os.environ.get("OPENAI_API_KEY"),
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
