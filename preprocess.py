# ==========================================================
# preprocess.py
# Text preprocessing for AI FAQ Chatbot
# ==========================================================

import string
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download only once
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

STOP_WORDS = set(stopwords.words("english"))


def preprocess(text):
    """
    Clean and preprocess text
    """

    if not isinstance(text, str):
        return ""

    # Lowercase
    text = text.lower()

    # Tokenize
    words = word_tokenize(text)

    cleaned = []

    for word in words:

        if word in string.punctuation:
            continue

        if word in STOP_WORDS:
            continue

        cleaned.append(word)

    return " ".join(cleaned)


def preprocess_list(sentences):

    processed = []

    for sentence in sentences:
        processed.append(preprocess(sentence))

    return processed


if __name__ == "__main__":

    sample = "What is Artificial Intelligence?"

    print(preprocess(sample))