
import random

def get_affiliate_link(topic):
    base_links = {
        "AI tools": "https://amzn.to/ai-tools",
        "productivity": "https://amzn.to/productivity",
        "budget drones": "https://amzn.to/budget-drones",
        "tech gadgets": "https://amzn.to/tech-gadgets"
    }
    for keyword, link in base_links.items():
        if keyword.lower() in topic.lower():
            return link
    return "https://amzn.to/default"

def embed_affiliate_link(content, topic):
    link = get_affiliate_link(topic)
    return f"{content}\n🔗 {link}"
