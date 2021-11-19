import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import nltk
from tinydb import TinyDB
import re

# Specify the working directory
workingdir = "corpora/"
# Punkt package for corpus exploring
nltk.download("punkt")


def db_to_corpus(db_path):
    """
    This method exports the data stored in tinydb to txt files as corpora of product descriptions!
    """
    # Read the json db
    db = TinyDB(db_path)
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


def sanitise_sentences(_sentences):
    """
    This method helps sanitise the data we got in the corpus, ignoring the trash to approach the most
    :param _sentences: A list of sentences to sanitise
    :return: A list of valuable sentences
    """
    results = []
    for sentence in _sentences:
        sentence = re.sub("\s*Réf : \d{6}\sR\d{13,20}", "", sentence)
        # If the sentence satisfies the condition that
        # It's not None, and it equals or is longer than the considered term "bio"
        if sentence is not False and len(sentence) >= 3:
            results.append(sentence.strip())
        else:
            # Otherwise, ignore it
            continue
    return results


def extract_sentences(corpus):
    """
    This method helps extracting sentences in a corpus to a txt file for tagging and annotation
    :param corpus: the corpus to extract
    :return: the sentences extracted
    """
    results = []
    # Get the list of corpus just in case
    items = [item for item in corpus.fileids()]
    for item in items:
        # Get the sentences within a corpus item
        sentences = corpus.raw(item).split(".")
        # Sanitise the data and put them into the results list
        results.extend((sanitise_sentences(sentences)))
    print("Extracted {0} sentences".format(len(results)))
    # Get the file and force it to write :(
    with open("data/sentences.txt", "w", encoding="UTF8") as sentencestxt:
        for record in results:
            # Write each sentence as a line with tab ending for marking later on
            sentencestxt.writelines(record+"\t\n")
        sentencestxt.close()
    return results


def extract_sentences_from_db(db_path):
    # Read the json db
    db = TinyDB(db_path)
    print(len(db.all()))
    # Get all product details
    details = [item for item in db.all()]
    # And product descriptions within them
    description = [item["description"] for item in details]
    # Check if the folder exists
    if not os.path.isdir(workingdir):
        # If not yet, simply create the folder
        os.mkdir(workingdir)
    filename = "data/sentences_for_tagging.txt"
    sentences = []
    for des in description:
        sentences.extend(sanitise_sentences(des.split(".")))

    with open(filename, "w", encoding="UTF8") as s4ttxt:
        for sen in sentences:
            s4ttxt.writelines(sen + "\t\n")
        s4ttxt.close()
    return len(sentences)

