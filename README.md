# Parte 1 - Questão 1: Gerador de texto com GPT-2

API em FastAPI que usa o modelo GPT-2 da HuggingFace (biblioteca `transformers`) para gerar uma continuação de texto a partir de uma frase enviada em JSON.

## Como executar

1. Crie e ative um ambiente virtual:
   ```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Rode a aplicação:
   ```
   uvicorn main:app --reload
   ```
4. Acesse http://127.0.0.1:8000/docs para testar.

Na primeira execução o modelo GPT-2 é baixado automaticamente, o que pode demorar alguns minutos.

## Exemplo de requisição

Rota `POST /gerar` com o corpo:

```json
{"frase": "Once upon a time"}
```

Resposta:

```json
{
  "entrada": "Once upon a time",
  "texto_gerado": "Once upon a time ..."
}
```