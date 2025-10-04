# Ollama Python - Testes com IA Local

Este projeto contém exemplos práticos de como usar a biblioteca Python do Ollama para interagir com modelos de IA locais, especificamente o modelo **Gemma 3**.

## 📋 Sobre o Projeto

Este repositório foi criado para testar e demonstrar diferentes formas de interagir com modelos de IA locais usando o Ollama. O projeto foca no modelo Gemma 3 e apresenta várias implementações de chat, desde versões simples até versões mais avançadas com streaming e histórico de conversas.

## 🚀 Pré-requisitos

- Python 3.8+
- Ollama instalado e rodando localmente
- Modelo Gemma 3 baixado no Ollama

### Instalação do Ollama

```bash
# Instalar o Ollama (Linux)
curl -fsSL https://ollama.ai/install.sh | sh

# Baixar o modelo Gemma 3
ollama pull gemma3
```

## 📦 Instalação

1. Clone este repositório:
```bash
git clone <url-do-repositorio>
cd ollama_py
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install ollama
```

## 📁 Estrutura do Projeto

- `chat.py` - Implementação básica de chat com resposta completa
- `chat-stream.py` - Chat com streaming (resposta em tempo real)
- `chat-async.py` - Chat assíncrono com streaming
- `chat-with-history.py` - Chat com histórico de conversas mantido

## 🎯 Como Usar

### Chat Básico
```bash
python chat.py
```
Implementação simples que faz uma pergunta e retorna a resposta completa.

### Chat com Streaming
```bash
python chat-stream.py
```
Mostra a resposta sendo escrita em tempo real, característica por característica.

### Chat Assíncrono
```bash
python chat-async.py
```
Versão assíncrona do chat com streaming, ideal para aplicações que precisam de melhor performance.

### Chat com Histórico
```bash
python chat-with-history.py
```
Mantém o contexto da conversa, permitindo perguntas de follow-up que fazem referência a mensagens anteriores.

## 🔧 Características

- **Modelo**: Gemma 3 (IA local)
- **Streaming**: Respostas em tempo real
- **Histórico**: Manutenção de contexto entre mensagens
- **Assíncrono**: Suporte a operações não-bloqueantes
- **Simplicidade**: Código limpo e fácil de entender

## 💡 Exemplos de Uso

Todos os scripts seguem o mesmo padrão:
1. Solicitam uma pergunta do usuário
2. Enviam para o modelo Gemma 3
3. Exibem a resposta (com ou sem streaming)
4. No caso do chat com histórico, mantêm o contexto para próximas perguntas

## 🛠️ Personalização

Você pode facilmente modificar os scripts para:
- Usar outros modelos do Ollama (trocar `'gemma3'` por outro modelo)
- Alterar o prompt padrão
- Adicionar validações de entrada
- Implementar persistência do histórico em arquivo

## 📝 Notas

- Certifique-se de que o Ollama está rodando antes de executar os scripts
- O modelo Gemma 3 deve estar baixado localmente
- Para melhor performance, use o chat assíncrono em aplicações web

## 🤝 Contribuições

Sinta-se à vontade para contribuir com melhorias, novos exemplos ou correções!

## 📄 Licença

Este projeto é para fins educacionais e de teste. Use conforme necessário.
