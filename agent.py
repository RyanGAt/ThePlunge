import time
from tools import trend_scraper, content_generator, voiceover_ttsmp3
from tools.monetization import monetization, affiliate_scraper
from publisher import twitter_poster

def run_cycle():
    print("🤖 AIPlunge content cycle started.")

    # Step 1: Get a trending topic
    trend = trend_scraper.get_trending_topic()
    print(f"🔥 Trending topic: {trend}")

    # Step 2: Generate content using OpenAI
    content = content_generator.generate_post(trend)
    print(f"📝 Content: {content}")

    # Step 3: Embed affiliate link
    content_with_link = affiliate_scraper.embed_affiliate_link(content, trend)
    print(f"🔗 With Affiliate Link:\n{content_with_link}")

    # Step 4: Generate voiceover MP3
    voiceover_ttsmp3.ttsmp3_speak(content_with_link)

    # Step 5: Find additional monetization (optional placeholder)
    monetization.find_affiliate_links(trend)

    # Step 6: Post to Twitter
    twitter_poster.post_to_twitter(content_with_link)

    print("✅ Cycle complete.")

if __name__ == "__main__":
    run_cycle()
