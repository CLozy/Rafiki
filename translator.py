from chat_extractor import extract_chat
from language_identifier import chooser 
from google_trans_new import google_translator
from transformers import pipeline
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer



model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

def verifier():
    return




def lang_translator(file_path):
    """
        function to translate the chats from detected language (assumed as source language) to  target language as english

        args: chats file path

        return: list of chats and their translations to english
    """
    
    # pipe = pipeline("text2text-generation", model="google/mt5-large")
    clean_chats = extract_chat(file_path)
    swh_text = []
    trans_swh_text = []
    eng_text = []

    tokenizer.src_lang = "swh"
    

    
    for chat in enumerate(clean_chats):
        lang = chooser(chat[1])  
        if lang[0] == 'swh':
            swh_text.append(chat[1])
            # translate_text = pipe(chat[1])
            encoded_zh = tokenizer(chat[1], return_tensors="pt")
            generated_tokens = model.generate(**encoded_zh, forced_bos_token_id=tokenizer.get_lang_id("en"))
            translate_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
            trans_swh_text.append(translate_text) 
        else:
            eng_text.append(chat[1])

    eng_text.append(trans_swh_text)
    all_chats = eng_text
    # print(swh_text[:5])
    # print(trans_swh_text[:5])
    return all_chats

     

print(lang_translator('data\chats\WhatsApp Chat with Yvette.txt'))
