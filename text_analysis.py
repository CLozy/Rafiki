

from nltk.stem import PorterStemmer
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize
import nltk

from nltk.corpus import reuters

# nltk.download('reuters')
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Sample Data
sample_text = reuters.raw(fileids=reuters.fileids(categories='crude')[0])
print(sample_text)

# TOKENIZATION
"""There are various types of tokenizers provided by nltk that handle splitting sentences  at certian levels, either
by sentence, word,regex,tweet etc"""
# sentence_tokenizer, tokenizes texts to sentences at punctuations

pst = PunktSentenceTokenizer()
print(pst.tokenize(sample_text))

# word tokenizer, splits text/sentences to individual words
print(word_tokenize(sample_text))

# STEMMING AND lEMMATIZATION
# Stemming is the process of morphological affixes from a word and reducing it to its stem, which is the root word, it takes in one word at a time.
stemmer = PorterStemmer()

plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
           'died', 'agreed', 'owned', 'humbled', 'sized',
           'meeting', 'stating', 'siezing', 'itemization',
           'sensational', 'traditional', 'reference', 'colonizer',
           'plotted']

singles = [stemmer.stem(plural) for plural in plurals]
print(singles)
# can use snawballstemmer to stem words language specific

"""Lemmatization is the process of converting a word to its lemma/base/dictionary form. It generally means transforming the word to its most basic, canonical, or lemma form. This involves stripping away inflections, derivational affixes, and considering the base form regardless of the word's grammatical part of speech.

For example:

Inflections: Converting plurals to singular forms (e.g., "dogs" to "dog").
Derivational affixes: Stripping away prefixes or suffixes that change the word's meaning (e.g., "unhappiness" to "happy").
Part of speech: Treating different grammatical forms of a word as a single lemma (e.g., "running" and "ran" reduced to "run").
helps in standardizing the representation of words"""

from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

print(wnl.lemmatize("dogs"))


#Stopword Analysis  Remove common words that do not contribute significantly to the meaning of the text.A predefined list of stopwords (common words like "the," "and," "is") is used to filter out these words.
