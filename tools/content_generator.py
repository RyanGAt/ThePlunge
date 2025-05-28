
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_post(topic):
    print(f"📝 Generating content for: {topic}")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                { "role": "system", "content": "You are an AI that writes viral short-form content for Twitter and YouTube Shorts." },
                { "role": "user", "content": f"Write a short, catchy script or post based on the topic: '{topic}'" }
            ],
            max_tokens=150,
            temperature=1.0
        )
        content = response.choices[0].message.content.strip()
        print(f"✅ Generated content: {content}")
        return content
    except Exception as e:
        print(f"❌ OpenAI content generation failed: {e}")
        return "AI content failed"
