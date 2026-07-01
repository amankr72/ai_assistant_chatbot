import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

json_file = BASE_DIR / "data" / "responses.json"

with open(json_file, "r") as file:
    responses = json.load(file)