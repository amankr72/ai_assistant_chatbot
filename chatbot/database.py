import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "hotels.db"


def find_hotels(params):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "SELECT name, area, price, stars FROM hotels WHERE 1=1"
    values = []

    if params["area"] is not None:
        query += " AND area = ?"
        values.append(params["area"])

    if params["price"] is not None:
        query += " AND price = ?"
        values.append(params["price"])

    if params["stars"] is not None:
        query += " AND stars = ?"
        values.append(params["stars"])

    if params["name"] is not None:
       query += " AND LOWER(name) = ?"
       values.append(params["name"].lower())    

    cursor.execute(query, values)

    results = cursor.fetchall()
    # print("Hotels:", results)
    conn.close()

    return results
if __name__ == "__main__":

    params = {
        "area": "north",
        "price": "mid",
        "stars": None,
        "name": None
    }

    # print(find_hotels(params))