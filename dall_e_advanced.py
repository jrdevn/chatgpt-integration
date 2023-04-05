import openai
import os
from dotenv import load_dotenv
import base64


def dall_e():
    openai.api_key = os.environ["API_KEY_CHATGPT"]


    response = openai.Image.create_variation(
        image=open("moto.png", "rb"), # png com menos de 4mb e mesma altura e largura
        size = "1024x1024",
        n = 1,
        response_format= "url" 
    )
    
    print(response["data"][0]["url"])
    

def dall_e_mask():
    openai.api_key = os.environ["API_KEY_CHATGPT"]


    response = openai.Image.create_edit(
        image=open("motomask.png", "rb"), # imagem original
        mask=open("DALL·E 2023-01-02 12.58.52.png", "rb"), # imagem com a mascara
        prompt="A motocycle with a big red airplane",
        size = "1024x1024",
        n = 1,
        response_format= "url" 
    )
    
    print(response["data"][0]["url"])
    
    
load_dotenv()
#dall_e()
dall_e_mask()