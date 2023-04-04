import openai
import os
from dotenv import load_dotenv
from myopenai import MyOpenAi

modelos = [
    "text-davinci-003",
    "text-curie-001",
    "text-babbage-001",
    "text-ada-001"
]


def basico():
    openai.api_key = os.environ["API_KEY_CHATGPT"]


    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="O que é Word Embedding? Você poderia também explicar o que é ngram?",
        max_tokens=2000,
        temperature=1, # a criatividade maxima 
        n = 4, ## 4 repostas em uma requisicao
    )

    for index, resposta in enumerate(response.choices):
        print(f"{index} resposta: {resposta.text}")


load_dotenv()
basico()