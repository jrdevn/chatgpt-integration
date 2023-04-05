import openai
import os
from dotenv import load_dotenv
import base64


def dall_e():
    openai.api_key = os.environ["API_KEY_CHATGPT"]


    response = openai.Image.create(
        prompt = "Crie uma imagem do Cristiano Ronaldo no Barcelona ",
        size = "512x512",
        n = 1,
        response_format= "b64_json" 
    )
    
    imagem = response["data"][0]["b64_json"]
    
    imagem = base64.b64decode(imagem)
    
    with open("resposta.png", "wb") as f:
        f.write(imagem)


load_dotenv()
dall_e()