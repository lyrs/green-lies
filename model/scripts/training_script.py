import random
from pathlib import Path

import spacy
from spacy.training import Example

PATH = "annotated_sentences_for_tagging.txt"


def prepare_data(path):
    res = []
    with open(path) as f:
        for line in f:
            elems = line.split("\t")
            res.append((elems[0], {"cats": {"GREEN": bool(int(elems[1])), "NOTGREEN": not bool(int(elems[1]))}}))
        return res


data = prepare_data(PATH)
print(data)

nlp = spacy.load('fr_dep_news_trf')

textcat = nlp.add_pipe("textcat")

textcat.add_label("GREEN")
textcat.add_label("NOTGREEN")

# with nlp.select_pipes(enable="textcat"):
optimizer = nlp.initialize()
# optimizer = nlp.begin_training()
for _ in range(30):
    losses = {}
    random.shuffle(data)
    # batches = minibatch(data, size=compounding(4., 32., 1.001))
    # for batch in batches:
    #     for text, annotation in batch:
    for text, annotation in data:
        nlp.update([Example.from_dict(nlp.make_doc(text), annotation)], losses=losses, sgd=optimizer)
    print("Losses", losses)

output_dir = Path('content/')
nlp.to_disk(output_dir)
print("Saved model to", output_dir)
