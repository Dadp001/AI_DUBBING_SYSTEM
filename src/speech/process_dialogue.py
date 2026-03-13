import json
import os


def clean_text(text):
    """
    Basic cleaning of transcript text
    """

    text = text.strip()

    # remove double spaces
    text = " ".join(text.split())

    return text


def process_transcript(input_file, output_file):

    print("Loading transcript...")

    with open(input_file, "r", encoding="utf-8") as f:
        segments = json.load(f)

    processed = []

    for seg in segments:

        text = clean_text(seg["text"])

        processed.append({"start": seg["start"], "end": seg["end"], "text": text})

    print("Saving processed dialogue...")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(processed, f, indent=4)

    print("Dialogue processing completed")


if __name__ == "__main__":

    input_file = "data/processed/transcript.json"
    output_file = "data/processed/dialogue.json"

    os.makedirs("data/processed", exist_ok=True)

    process_transcript(input_file, output_file)
