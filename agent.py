
import time
from tools import trend_scraper, voiceover_ttsmp3, monetization

def run_cycle():
    print("🤖 AIPlunge content cycle started.")
    trend = trend_scraper.get_trending_topic()
    content = f"Here's a quick dive into: {trend}"
    voiceover_ttsmp3.ttsmp3_speak(content)
    monetization.find_affiliate_links(trend)
    print("✅ Cycle complete.")

if __name__ == "__main__":
    run_cycle()
