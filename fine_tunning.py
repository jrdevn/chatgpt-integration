import openai
import os
from dotenv import load_dotenv


def fine_tune():
    openai.api_key = os.environ["API_KEY_CHATGPT"]


    response = openai.Completion.create(
        model="ft-5hfmPefiRqn3MkwF4yABpWAG",
        prompt="Qual horário de funcionamento?",
        max_tokens=50,
        temperature=0
    )

    for index, resposta in enumerate(response.choices):
        print(f"{index+1} resposta: {resposta.text}")


load_dotenv()
fine_tune()