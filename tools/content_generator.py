import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_post(topic):
    if not GROQ_API_KEY:
        print("❌ GROQ_API_KEY not found in environment variables.")
        return "AI content failed"

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that writes short, engaging social media posts on trending topics."
            },
            {
                "role": "user",
                "content": f"Write a short social media post about: {topic}"
            }
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print(f"❌ Groq content generation failed: {e}")
        return "AI content failed"
