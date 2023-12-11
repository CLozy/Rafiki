import nltk

from nltk.corpus import reuters
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize
# nltk.download('reuters')
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

#Sample Data
sample_text = reuters.raw(fileids=reuters.fileids(categories='crude')[0])
print(sample_text)

#TOKENIZATION
"""There are various types of tokenizers provided by nltk that handle splitting sentences  at certian levels, either
by sentence, word,regex,tweet etc"""
#sentence_tokenizer

pst = PunktSentenceTokenizer()
print(pst.tokenize(sample_text))

#word tokenizer
print(word_tokenize(sample_text))

