
import requests
import random

def get_trending_topic():
    # Placeholder logic - simulate Google Trends result
    trends = [
        "AI productivity hacks",
        "2025 side hustles",
        "Best budget drones",
        "How to get started in FPV",
        "Make money with AI tools"
    ]
    chosen = random.choice(trends)
    print(f"🔥 Trending topic: {chosen}")
    return chosen
