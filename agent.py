import time
from tools import trend_scraper, content_generator, voiceover_ttsmp3, monetization

def run_cycle():
    print("🤖 AIPlunge content cycle started.")

    # Step 1: Get a trending topic
    trend = trend_scraper.get_trending_topic()

    # Step 2: Use OpenAI to generate actual content
    content = content_generator.generate_post(trend)

    # Step 3: Turn content into a voiceover MP3
    voiceover_ttsmp3.ttsmp3_speak(content)

    # Step 4: Find monetization opportunities
    monetization.find_affiliate_links(trend)

    print("✅ Cycle complete.")

if __name__ == "__main__":
    run_cycle()
