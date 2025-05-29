
import os
import tweepy

def post_to_twitter(content):
    try:
        auth = tweepy.OAuth1UserHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET"),
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_SECRET")
        )
        api = tweepy.API(auth)
        tweet = api.update_status(content)
        print(f"🐦 Tweet posted: https://twitter.com/user/status/{tweet.id}")
        return True
    except Exception as e:
        print(f"❌ Failed to post tweet: {e}")
        return False
