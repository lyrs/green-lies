import spacy
from tinydb import TinyDB
from spacy.tokens import DocBin
# from spacy.tokens import Doc

# --------------------------------------------------

# Create a word list for the doc
# words = ["bonjour", "le", "monde", "!"]

# Spaces is the list of boolean deciding whether it's a space after the corresponding word.
# For example, with ["hello","world","!"] and spaces=[True,True,True], we get "hello world ! " as result
# The list of space determiners must have the same length with the list of words.
# spaces = [True, True, False, False]
# Create a doc based on the vocab, words, and spaces
# doc = Doc(nlp.vocab, words=words, spaces=spaces)
# Exploration: try printing the texts in nlp.vocab on your own

# --------------------------------------------------

# Run python -m spacy download en_core_web_sm using the command line before reaching the next line
pipeline = ["fr_core_news_sm"]
# Load the spacy pipeline
nlp = spacy.load(pipeline[0])
# Create a doc with a specific string
doc = nlp("Greenlies est prêt!")
# Load data from tinydb
db = TinyDB("db-nocibe.json")
# Get the product details
details = [item for item in db.all()]
# And product descriptions within them
description = [item["description"] for item in details]
# Create a doc bin to store documents
doc_bin = DocBin(attrs=["LEMMA"])
for item in description:
    single_doc = nlp(str(item))
    doc_bin.add(single_doc)
# Pour all the docs into the serialised file
doc_bin.to_disk("./data/corpus.spacy")