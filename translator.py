from chat_extractor import extract_chat
from language_identifier import chooser

file_path = 'data\chats\WhatsApp Chat with Yvette.txt'

def verifier():
    return


def lang_translator(file_path):
    """
        function to translate the chats from detected language (assumed as source language) to  target language as english

        args: chats file path

        return: list of chats and their translations to english
    """
    clean_chats = extract_chat(file_path)
    for chat in enumerate(clean_chats):
        lang = chooser(chat[1])
        # print(lang)

        # if chat[0] == 10:
        #     break


# print(lang_translator(file_path))
