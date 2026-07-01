import joblib
import spacy
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "model.pkl")
encoder = joblib.load(BASE_DIR / "label_encoder.pkl")

nlp = spacy.load("en_core_web_md")


def predict_intent(message):

    doc = nlp(message)

    vector = doc.vector.reshape(1, -1)

    prediction = model.predict(vector)

    return encoder.inverse_transform(prediction)[0]


if __name__ == "__main__":

    while True:

        message = input("You: ")

        if message.lower() == "exit":
            break

        print("Intent:", predict_intent(message))