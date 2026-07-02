import pandas as pd
import joblib
from pathlib import Path
import spacy
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent.parent

csv_file = BASE_DIR / "data" / "intents.csv"

df = pd.read_csv(csv_file)

print(df.head())
print()
print(df.shape)

nlp = spacy.load("en_core_web_sm")

# Convert sentences to vectors
X = []

for sentence in df["text"]:
    doc = nlp(sentence)
    X.append(doc.vector)
X = np.array(X)



# Encode intent labels
encoder = LabelEncoder()
y = encoder.fit_transform(df["intent"])

print(df["intent"].value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
# Train SVM


model = SVC(
    kernel="linear",
    C=1.0,
    probability=True,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.2f}")

labels = np.unique(np.concatenate((y_test, y_pred)))

print(
    classification_report(
        y_test,
        y_pred,
        labels=labels,
        target_names=encoder.inverse_transform(labels)
    )
)
MODEL_DIR = Path(__file__).resolve().parent

joblib.dump(model, MODEL_DIR / "model.pkl")
joblib.dump(encoder, MODEL_DIR / "label_encoder.pkl")

print("\nModel saved successfully!")
