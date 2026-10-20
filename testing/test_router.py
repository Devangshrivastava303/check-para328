from dotenv import load_dotenv
import os
import httpx

load_dotenv()

api_key=os.getenv("OPENROUTER_API_KEY")
if api_key:
    print("found")
else:
    print("nahi mili!")

#for open-router header 
headers={
    "Authorization":f"Bearer {api_key}",
    "Content-Type":"application/json",
}

body={
    "model":"mistralai/mistral-small-3.2-24b-instruct:free​‌",
    "messages":[{"role": "user", "content": "Say hello in exactly 5 words"}
    ],

    "max_tokens": 50,
    "temperature": 0.7,
}
url="https://openrouter.ai/api/v1/chat/completions"
with httpx.Client(timeout=30.0) as client:
    response=client.post(url,headers=headers,json=body)
print(f"Status: {response.status_code}")
print(f"Headers: {dict(response.headers)}")

data = response.json()
print(data)

if response.status_code == 200:
    answer = data["choices"][0]["message"]["content"]
    tokens = data["usage"]["total_tokens"]
    model_used = data["model"]
    
    print(f"Model: {model_used}")
    print(f"Answer: {answer}")
    print(f"Tokens: {tokens}")
else:
    print(f"Error: {data}")