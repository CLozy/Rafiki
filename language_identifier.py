
import joblib
import re


langiso2iso = {
    'swa': 'swh',
    'eng': 'eng'
}

eng_pattern = re.compile('^((okay|y|yes|no way|hi)([,?.!-=:;*]*?))$',re.I)
swh_pattern = re.compile('^((jambo|fiti|do ivo|habari|asanti|asante|ahsanti|ahsante|bora|eeh)([,?.!-=:;*]*?))$',re.I)

model = joblib.load("models\lidentifier-eng-swa.sav")


def regex_classifier(message):

    if re.search(pattern=eng_pattern, string=message):
        return 'eng'
    if re.search(pattern=swh_pattern, string=message):
        return 'swh'

    return None

def chooser(message):

    obj = regex_classifier(message)
    if obj:
        detected_lang = obj
    else:
        detected_lang = model.predict([message])[0]
        detected_lang = langiso2iso[detected_lang]
    
    return (detected_lang, 1)


# print(chooser('Hi mimi naitwa charleen lozi'))