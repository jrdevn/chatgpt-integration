import os
from dotenv import load_dotenv
from myopenai import MyOpenAi

def byclass():
    chat = MyOpenAi("Quantos titulos tem o São Paulo FC?", "text-davinci-003", 3, 1000, 1, os.environ["API_KEY_CHATGPT"])
    response = chat.callgpt()
    for res in response:
        print(res)

load_dotenv()
byclass()