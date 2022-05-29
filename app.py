from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"Módulo 6": "Lição de casa 6"}


class Operacoes(BaseModel):
    valor_1 = int
    valor_2 = int
    oper = str


@app.post("/soma")
async def opSoma(valor_1: int, valor_2: int, oper: str):
    if oper == 'sm'.lower() or '+':
        soma = (valor_1 + valor_2)
        return soma
