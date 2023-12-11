import nltk

from nltk.corpus import reuters
# nltk.download('reuters')
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

#Sample Data
sample_text = reuters.raw(fileids=reuters.fileids(categories='crude')[0])

#TOKENIZATION
"""There are various types of tokenizers provided by nltk that handle splitting sentences  at certian levels, either
by sentence, word,regex,tweet etc"""
#sentence_tokenizer
"""Using PunktSentenceTokenizer"""