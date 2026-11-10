from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Gerador de texto com GPT-2")

# o modelo é carregado uma vez, quando a aplicação inicia
gerador = pipeline("text-generation", model="gpt2")


class Entrada(BaseModel):
    frase: str


@app.post("/gerar")
def gerar(entrada: Entrada):
    resultado = gerador(
        entrada.frase,
        max_new_tokens=50,
        num_return_sequences=1,
        pad_token_id=50256,
    )
    return {"entrada": entrada.frase, "texto_gerado": resultado[0]["generated_text"]}