from ollama import chat

pergunta=input("O que você precisa saber hoje? ")

messages = [
  {
    'role': 'user',
    'content': pergunta+' Responda de forma objetiva.',
  },
]

for part in chat('gemma3', messages=messages, stream=True):
  print(part['message']['content'], end='', flush=True)