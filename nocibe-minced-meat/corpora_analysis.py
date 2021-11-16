import csv

import pandas as pd
import numpy as np
from tinydb import TinyDB
import nltk
import csv
import os

from nltk.corpus import stopwords

nltk.download("stopwords")

french_stop_words = stopwords.words("french")


def create_tsv_db():
    db = TinyDB("db-nocibe.json")
    items = [itm for itm in db.all()]

    workingdir = "data/"
    # Check if the folder exists
    if not os.path.isdir(workingdir):
        # If not yet, simply create the folder
        os.mkdir(workingdir)
    with open("data/db-nocibe.tsv", "w", encoding="utf-8") as tsvdb:
        writer = csv.writer(tsvdb, delimiter="\t")
        writer.writerow(["brand", "name", "labels", "description", "ingredients"])
        for item in items:
            writer.writerow([item["brand"], item["name"], item["labels"], item["description"], item["ingredients"]])
        tsvdb.close()
    pass

#create_tsv_db()

df = pd.read_csv("data/db-nocibe.tsv", sep="\t")
