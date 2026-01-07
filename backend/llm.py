import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_llm(prompt: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }

    r = requests.post(url, headers=headers, json=payload, timeout=30)

    if r.status_code != 200:
        return "LLM_ERROR"

    return r.json()["choices"][0]["message"]["content"]
