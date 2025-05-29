import time
from tools import trend_scraper, content_generator, voiceover_ttsmp3, video_generator, background_generator
from tools.monetization.affiliate_scraper import get_affiliate_link, embed_affiliate_link
from tools import monetization
from publisher import twitter_poster, youtube_uploader

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
    voiceover_path = voiceover_ttsmp3.ttsmp3_speak(content_with_link)

    # Step 5: Download background image automatically
    background_generator.download_background(trend)

    # Step 6: Generate a video using the voiceover + background image
    video_path = video_generator.generate_video_with_voiceover(
        audio_file=voiceover_path,
        image_file="assets/background.jpg",
        output_file="output/latest/sample_short.mp4"
    )

    # Step 7: Post to Twitter
    twitter_poster.post_to_twitter(content_with_link)

    # Step 8: Upload to YouTube
    if video_path:
        youtube_uploader.upload_video(
            file_path=video_path,
            title=trend,
            description=content_with_link,
            tags=["AI", "automation", "shorts"]
        )

    print("✅ Cycle complete.")

if __name__ == "__main__":
    run_cycle()
