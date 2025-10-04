from ollama import chat

messages = []

while True:
    # Pergunta ao usuário o que ele precisa saber e salva na variável user_input
    user_input = input("O que você precisa saber hoje? ")

    # Faz a chamada ao modelo e salva na variável response_stream
    response_stream = chat(
        "gemma3",
        messages=[*messages, {"role": "user", "content": user_input + " Responda de forma objetiva."}],
        stream=True,
    )

    # Inicializa a variável assistant_content como uma string vazia
    assistant_content = ""

    # Itera sobre os pedaços do stream
    # Para cada evento, se o evento tiver delta (texto incremental), imprime
    # e salva na variável assistant_content
    for event in response_stream:
        # Se o evento tiver delta (texto incremental), imprime e salva na variável assistant_content
        if hasattr(event, "message") and hasattr(event.message, "content"):
            print(event.message.content, end="", flush=True)
            assistant_content += event.message.content

    # Salva no histórico a pergunta e a resposta
    messages += [
        {"role": "user", "content": user_input + " Responda de forma objetiva."},
        {"role": "assistant", "content": assistant_content},
    ]
    # Imprime uma linha em branco
    print("\n")
