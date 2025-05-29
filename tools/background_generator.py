
import os
import requests
from pathlib import Path

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
PEXELS_API_URL = "https://api.pexels.com/v1/search"

def download_background(topic, output_path="assets/background.jpg"):
    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": topic,
        "per_page": 1
    }

    try:
        response = requests.get(PEXELS_API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if data["photos"]:
            image_url = data["photos"][0]["src"]["landscape"]
            img_data = requests.get(image_url).content

            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, "wb") as f:
                f.write(img_data)

            print(f"🖼️ Background downloaded for topic '{topic}' → {output_path}")
            return str(output_path)
        else:
            print("⚠️ No images found for topic.")
            return None
    except Exception as e:
        print(f"❌ Failed to download background: {e}")
        return None

# Test run
if __name__ == "__main__":
    download_background("AI technology")
