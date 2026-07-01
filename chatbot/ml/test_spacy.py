import spacy

nlp = spacy.load("en_core_web_md")

text = "I want a cheap hotel in the north"

doc = nlp(text)

print("Text:", doc.text)
print("Vector Shape:", doc.vector.shape)
print("First 10 Values:", doc.vector[:10])