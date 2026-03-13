from moviepy import VideoFileClip
import os


def extract_audio(video_path, output_path):
    """
    Extract audio from a video file.
    """

    print("Loading video...")

    video = VideoFileClip(video_path)

    print("Extracting audio...")

    video.audio.write_audiofile(output_path)

    print("Audio extraction completed")


if __name__ == "__main__":

    video_path = "data/raw/test_video.mov"
    output_path = "data/processed/audio.wav"

    os.makedirs("data/processed", exist_ok=True)

    extract_audio(video_path, output_path)
