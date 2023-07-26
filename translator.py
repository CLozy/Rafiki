from chat_extractor import extract_chat
from language_identifier import chooser 
from google_trans_new import google_translator
from transformers import pipeline

file_path = 'data\chats\WhatsApp Chat with Yvette.txt'

def verifier():
    return






def lang_translator(file_path):
    """
        function to translate the chats from detected language (assumed as source language) to  target language as english

        args: chats file path

        return: list of chats and their translations to english
    """
    pipe = pipeline("text2text-generation", model="masakhane/m2m100_418M_swa_en_rel_news_ft")
    clean_chats = extract_chat(file_path)
    swh_text = []
    trans_swh_text = []
    for chat in enumerate(clean_chats):
        lang = chooser(chat[1])  
        if lang[0] == 'swh':
            swh_text.append(chat[1])
            translate_text = pipe(chat[1])
            trans_swh_text.append(translate_text[0]['generated_text']) 
    
    print(swh_text[:5])
    print(trans_swh_text[:5])

     

lang_translator(file_path)
