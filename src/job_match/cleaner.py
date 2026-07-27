import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

def clean_text(text):
    # lower case 

    text = text.lower()

    # tokenize
    tokens = word_tokenize(text)

    #remove punctuation and stop words

    stop_words = set(stopwords.words('english'))

    filtered = []

    for token in tokens:
        if token not in stop_words and token not in string.punctuation:
            filtered.append(token)


    stemmer = PorterStemmer()

    stemmed = []
    for token in filtered:
        stemmed.append(stemmer.stem(token))


    #return cleaned tokens as a list
    return stemmed
