import spacy
from spacy.tokens import DocBin

PATH = "annotated_sentences_for_tagging.txt"

nlp = spacy.load("fr_dep_news_trf")

db = DocBin()
with open(PATH) as f:
    for line in f:
        elems = line.split("\t")
        text = elems[0]
        anno = {"cats": {"GREEN": bool(int(elems[1])), "NOTGREEN": not bool(int(elems[1]))}}
        doc = nlp.make_doc(text)
        doc.cats = anno['cats']
        db.add(doc)

db.to_disk("train.spacy")
