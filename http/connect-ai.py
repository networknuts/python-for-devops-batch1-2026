import requests
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

url = "https://api.openai.com/v1/responses"

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

system_prompt = "You are a note taking assistant, summarize given data in professional meeting note summary"
raw_file = open("notes.txt","r")
raw_data = raw_file.read()
raw_file.close()

payload = {
    "model": "gpt-4.1",
    "input": [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": raw_data
        }
    ]
}

response = requests.post(url,headers=headers,json=payload)

print(response.json()["output"][0]["content"][0]['text'])
