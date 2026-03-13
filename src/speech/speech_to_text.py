import whisper
import json
import os


def transcribe_audio(audio_path, output_json):

    print("Loading Whisper model...")

    model = whisper.load_model("base")

    print("Transcribing audio...")

    result = model.transcribe(audio_path, fp16=False)

    transcripts = []

    for segment in result["segments"]:
        transcripts.append(
            {"start": segment["start"], "end": segment["end"], "text": segment["text"]}
        )

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(transcripts, f, indent=4)

    print("Transcription saved")


if __name__ == "__main__":

    audio_path = "data/processed/audio.wav"
    output_json = "data/processed/transcript.json"

    os.makedirs("data/processed", exist_ok=True)

    transcribe_audio(audio_path, output_json)
