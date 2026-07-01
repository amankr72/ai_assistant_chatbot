import re
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

csv_file = BASE_DIR / "data" / "intents.csv"

df = pd.read_csv(csv_file)

# Dictionary:
# {
#   "greet": ["hello","hi"],
#   "thanks": ["thanks","thank you"]
# }

keywords = {}

for _, row in df.iterrows():

    intent = row["intent"]

    text = row["text"].lower()

    if intent not in keywords:
        keywords[intent] = []

    keywords[intent].append(text)

patterns = {}

for intent, examples in keywords.items():

    escaped_examples = [re.escape(example) for example in examples]

    pattern = r"\b(" + "|".join(escaped_examples) + r")\b"

    patterns[intent] = re.compile(pattern, re.IGNORECASE)  



