import openai
import os
from dotenv import load_dotenv


def contextwith():
    openai.api_key = os.environ["API_KEY_CHATGPT"]

    contexto = '''Empresa com mais de 10 anos no mercado de manutenção e fabricação de esquadrias de alumínio , 
    manutenção em persianas manual e motorizada troca de acessórios em geral , 
    roldanas , cadarço de persianas'''

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= contexto + "Vocês trabalham com persianas?",
        max_tokens=1000,
    )

    for index, resposta in enumerate(response.choices):
        print(f"{index+1} resposta: {resposta.text}")


load_dotenv()
contextwith()