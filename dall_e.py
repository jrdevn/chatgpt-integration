import openai
import os
from dotenv import load_dotenv


def dall_e():
    openai.api_key = os.environ["API_KEY_CHATGPT"]

    response = openai.Image.create(
        prompt = "Crie uma imagem 3D do homem aranha da cor rosa",
        size = "512x512",
        n = 1,
        response_format= "url" ## ou json base64
    )
    
    print(response["data"][0]["url"])


load_dotenv()
dall_e()