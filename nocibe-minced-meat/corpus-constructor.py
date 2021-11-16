import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import nltk
from tinydb import TinyDB


# Specify the working directory
workingdir = "corpora/"
# Punkt package for corpus exploring
nltk.download("punkt")


def db_to_corpus():
    """
    This method exports the data stored in tinydb to txt files as corpora of product descriptions!
    """
    # Read the json db
    db = TinyDB("db-nocibe.json")
    # Get all product details
    details = [item for item in db.all()]
    # And product descriptions within them
    description = [item["description"] for item in details]
    # Check if the folder exists
    if not os.path.isdir(workingdir):
        # If not yet, simply create the folder
        os.mkdir(workingdir)
    # The prefix for corpora file names
    filename = "nocibe"
    # Incrementor for naming
    filecount = 0
    # Loop over the retrieved descriptions
    for item in description:
        # Increase the forking file so-called index by 1 just for naming
        filecount += 1
        # Open the file and overwrite it's content
        with open(workingdir + filename + str(filecount) + ".txt", "w", encoding="utf-8") as record:
            record.write(item)
    # Return the number of affected files
    return filecount


def read_corpus():
    """
    This method helps you with reading the directory to return all the corpora
    """
    return PlaintextCorpusReader(workingdir, ".*")



