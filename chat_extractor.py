import re
import emoji



def extract_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as chat:
        text = chat.read()


    # Extract the chat messages using regular expressions
    chat_messages = re.findall(r'(?<=: )[\w\s.,!?-]+', text)
    # print(chat_messages)

    chats = []
    for string in chat_messages:
        new_string = string.split("\n")[0]
        chats.append(new_string)

    return chats



# print(extract_chat(file_path=file_path))
