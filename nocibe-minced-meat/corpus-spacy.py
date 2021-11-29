import spacy
from tinydb import TinyDB
from spacy.tokens import DocBin
# from spacy.tokens import Doc
from spacy.tokenizer import Tokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt


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


def export_spacy_corpus():
    # Run python -m spacy download fr_core_web_sm using the command line before reaching the next line
    pipeline = ["fr_core_news_sm"]
    # Load the spacy pipeline
    nlp = spacy.load(pipeline[0])
    # Stop words for french
    fr_stopwords = nlp.Defaults.stop_words
    # Load data from tinydb
    db = TinyDB("../db.json")
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
    doc_bin.to_disk("data/corpus.spacy")


# def remove_stop_words(dir):
#     with open(dir, encoding="utf-8") as sentencestxt:
#         sentences = sentencestxt.readlines()
#     pipeline = spacy.load("fr_core_news_sm")
#     stop_words = pipeline.Defaults.stop_words
#     purged_sentences = []
#     for sentence in sentences:
#         text_tokens = sentence.split(" ")
#         purged_sentence = [token.strip() for token in text_tokens if token not in stop_words]
#         purged_sentences.append(purged_sentence)
#     return purged_sentences
#
#
# def purify_and_merge_sentences(dir):
#     purged_sentences = remove_stop_words(dir)
#     words = []
#     for sentence in purged_sentences:
#         [words.append(word) for word in sentence]
#     return words
#
#
# def create_word_cloud():
#     words = purify_and_merge_sentences("data/sentences_for_tagging.txt")
#     wc = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(" ".join(words))
#     plt.figure()
#     plt.imshow(wc, interpolation="bilinear")
#     plt.axis("off")
#     plt.show()

def load_from_txt(dir):
    sentences = []
    results = []
    with open(dir, encoding="utf-8") as file:
        sentences = file.readlines()
    pipeline = spacy.load("fr_core_news_sm")
    docs = [pipeline(sentence) for sentence in sentences]
    stop_words = pipeline.Defaults.stop_words
    for doc in docs:
        [results.append(token) for token in doc if token.text.lower() not in stop_words]
    return results


# results = load_from_txt("data/sentences_for_tagging.txt")

def create_word_cloud():
    tokens = load_from_txt("data/sentences_for_tagging.txt")
    words = []
    for token in tokens:
        words.append(token.text)
    wc = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(" ".join(words))
    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

create_word_cloud()