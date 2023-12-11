
from transformers import pipeline
from translator import lang_translator



file_path = 'data\chats\WhatsApp Chat with Yvette.txt'

chats = lang_translator(file_path)
# Join the list elements into a single string using a newline character as the delimiter
chats_string = '\n'.join(chats)

# Print the resulting string
print(chats_string)
def chat_emotions(chats):
    classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
    prediction = classifier(chats )
    print(prediction)



def chat_sentiment():
    classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
    prediction = classifier("I love using transformers. The best part is wide range of support and its easy to use", )
    print(prediction)

def chat_stars():
    classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
    prediction = classifier("I love using transformers. The best part is wide range of support and its easy to use", )
    print(prediction)


chat_emotions(chats)