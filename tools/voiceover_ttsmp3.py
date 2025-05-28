
import requests
import os
from pathlib import Path
import time

def ttsmp3_speak(text, filename="voiceover.mp3", voice="Brian", retries=3):
    url = "https://ttsmp3.com/makemp3_new.php"
    payload = {
        "msg": text,
        "lang": voice,
        "source": "ttsmp3"
    }

    headers = {
        "Origin": "https://ttsmp3.com",
        "Referer": "https://ttsmp3.com/",
        "User-Agent": "Mozilla/5.0"
    }

    for attempt in range(retries):
        try:
            response = requests.post(url, data=payload, headers=headers, timeout=15)
            response.raise_for_status()
            result = response.json()

            if result.get("URL"):
                audio_url = result["URL"]
                audio_data = requests.get(audio_url).content

                output_dir = Path("output/latest")
                output_dir.mkdir(parents=True, exist_ok=True)

                file_path = output_dir / filename
                with open(file_path, "wb") as f:
                    f.write(audio_data)

                print(f"✅ Voiceover saved to {file_path}")
                return str(file_path)
            else:
                print("❌ TTSMP3 failed to return a valid URL.")
                return None

        except Exception as e:
            print(f"Error on attempt {attempt+1}: {e}")
            time.sleep(2)

    return None
