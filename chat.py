from ollama import chat
from ollama import ChatResponse

pergunta=input("O que você precisa saber hoje? ")

response: ChatResponse = chat(model='gemma3', messages=[
  {
    'role': 'user',
    'content': pergunta+'Responda de forma objetiva.',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)