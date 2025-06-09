import requests

# 🔑 Replace with your Together API Key
API_KEY = "249f7cd0b37db86a677c420a649155c316bb4d5c1d4111ea8d47f698251f3a98"

API_URL = "https://api.together.xyz/v1/chat/completions"


headers = {
    "Authorization": f"Bearer " + API_KEY,
    "Content-Type": "application/json"
}

payload = {
    "model": "meta-llama/Llama-3-8b-chat-hf",  # Faster model
    "messages": [
        {"role": "user", "content": "Hey, can you hear me?"}
    ],
    "temperature": 0.7,
    "max_tokens": 200,
    "top_p": 0.9
}

try:
    response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    print("✅ Response:")
    print(response.json()["choices"][0]["message"]["content"])
except requests.exceptions.RequestException as e:
    print("❌ Error during API call:")
    print(e)
