import time
from tools import trend_scraper, content_generator, voiceover_ttsmp3, monetization, twitter_poster

def run_cycle():
    print("🤖 AIPlunge content cycle started.")

    # Step 1: Get a trending topic
    trend = trend_scraper.get_trending_topic()

    # Step 2: Generate content using OpenAI
    content = content_generator.generate_post(trend)

    # Step 3: Generate voiceover MP3
    voiceover_ttsmp3.ttsmp3_speak(content)

    # Step 4: Find affiliate links (placeholder)
    monetization.find_affiliate_links(trend)

    # Step 5: Post to Twitter
    twitter_poster.post_to_twitter(content)

    print("✅ Cycle complete.")

if __name__ == "__main__":
    run_cycle()
