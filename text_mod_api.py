import unicodedata, re
import nltk
from nltk.corpus import stopwords
from collections import Counter


# start https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html
def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words


def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words


# end https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html

def remove_words_from_list(word_list, forbidden_list):
    """Remove any word from the specific list"""
    return_list = []
    forbidden_list = [single_forbid.lower() for single_forbid in forbidden_list]
    for single_word in word_list:
        if single_word.lower() not in forbidden_list:
            return_list.append(single_word)
    return return_list


def make_lowercase(word_list):
    return [single_word.lower() for single_word in word_list]


def remove_links_from_list(word_list):
    """Remove any word that starts with http"""
    return_list = []
    for single_word in word_list:
        if re.search(r'^http.+', single_word) != None:
            pass
        else:
            return_list.append(single_word)
    return return_list


def normalize_string_to_dict(word_string):

    #I super hate this coding pattern
    words = remove_stopwords(word_string.split(" "))
    words = make_lowercase(words)
    words = remove_words_from_list(words, ["&amp;", "rt"])
    words = remove_links_from_list(words)
    words = remove_non_ascii(words)
    words = remove_punctuation(words)

    words = nltk.word_tokenize(" ".join(words))

    words = remove_stopwords(words)

    word_dict = Counter(words)

    return dict(word_dict)
