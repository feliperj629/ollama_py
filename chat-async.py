import asyncio

from ollama import AsyncClient


async def main():

  pergunta=input("O que você precisa saber hoje? ")

  messages = [
    {
      'role': 'user',
      'content': pergunta,
    },
  ]

  client = AsyncClient()
  
  print("\nResposta:")
  print("-" * 50)
  
  # Usar stream para ver a resposta sendo escrita em tempo real
  stream = await client.chat('gemma3', messages=messages, stream=True)
  async for chunk in stream:
    # Imprimir cada pedaço da resposta conforme ela chega
    print(chunk['message']['content'], end='', flush=True)
  
  print("\n" + "-" * 50)


if __name__ == '__main__':
  asyncio.run(main())