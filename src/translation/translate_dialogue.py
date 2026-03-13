import json
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def translate_dialogue(input_file, output_file):

    print("Loading translation model...")

    model_name = "Helsinki-NLP/opus-mt-en-hi"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    print("Loading dialogue file...")

    with open(input_file, "r", encoding="utf-8") as f:
        dialogues = json.load(f)

    translated = []

    for d in dialogues:

        text = d["text"]

        inputs = tokenizer(text, return_tensors="pt", padding=True)

        outputs = model.generate(**inputs)

        translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        translated.append(
            {
                "start": d["start"],
                "end": d["end"],
                "original": text,
                "translated": translated_text,
            }
        )

    print("Saving translated dialogue...")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(translated, f, indent=4, ensure_ascii=False)

    print("Translation completed")


if __name__ == "__main__":

    input_file = "data/processed/dialogue.json"
    output_file = "data/processed/translated_dialogue.json"

    os.makedirs("data/processed", exist_ok=True)

    translate_dialogue(input_file, output_file)
