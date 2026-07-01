import re
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "hotels.db" 

AREA = [
    "north",
    "south",
    "east",
    "west",
    "center"
]

PRICE_MAP = {
    "cheap": "lo",
    "low": "lo",
    "budget": "lo",
    "lo": "lo",

    "mid": "mid",
    "medium": "mid",

    "expensive": "hi",
    "high": "hi",
    "luxury": "hi",
    "premium": "hi",
    "hi": "hi"
}

def extract_entities(message):

    message = message.lower()

    entities = {}

    # -----------------------
    # Area
    # -----------------------
    for area in AREA:

        if re.search(rf"\b{re.escape(area)}\b", message):

            entities["area"] = area

    # -----------------------
    # Price
    # -----------------------
    for word, db_price in PRICE_MAP.items():

        if re.search(rf"\b{re.escape(word)}\b", message):

            entities["price"] = db_price

    # -----------------------
    # Stars
    # -----------------------
    match = re.search(r"\b([1-5])(?:\s*|-)?star[s]?\b", message)

    if match:
        entities["stars"] = int(match.group(1))
# -----------------------
# Hotel Name
# -----------------------

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM hotels")

    hotel_names = [row[0].lower() for row in cursor.fetchall()]

    conn.close()

    for hotel in hotel_names:
        if hotel in message:
            entities["name"] = hotel
            break
    return entities