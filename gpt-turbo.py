import openai
import os
from dotenv import load_dotenv


def gpt_turbo():
    openai.api_key = os.environ["API_KEY_CHATGPT"]

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "Você está respondendo perguntas"},
            {"role": "user", "content": "Quem foi Carlos Drummond Andrade?"},
            {"role": "assistant", "content": "Carlos Drummond Andrade foi um poeta"},
            {"role": "user", "content": "Quais poemas o Carlos Drummond escreveu?"}
        ],
        temperature = 0
    )

    print(response["choices"][0]["message"]["content"])


load_dotenv()
gpt_turbo()