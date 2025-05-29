
from moviepy.editor import AudioFileClip, ImageClip
from pathlib import Path

def generate_video_with_voiceover(audio_file="output/latest/voiceover.mp3", 
                                  image_file="assets/background.jpg", 
                                  output_file="output/latest/sample_short.mp4"):
    try:
        audio = AudioFileClip(audio_file)
        image = ImageClip(image_file).set_duration(audio.duration).set_audio(audio).resize(height=720)
        image.write_videofile(output_file, fps=24)
        print(f"🎞️ Video created: {output_file}")
        return output_file
    except Exception as e:
        print(f"❌ Failed to generate video: {e}")
        return None

# Run standalone for testing
if __name__ == "__main__":
    generate_video_with_voiceover()
