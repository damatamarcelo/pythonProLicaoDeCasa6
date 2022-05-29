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


@app.post("/subtracao")
async def opSubtracao(valor_1: int, valor_2: int, oper: str):
    if oper == 'sb'.lower() or '-':
        subtracao = (valor_1 - valor_2)
        return subtracao


@app.post("/multiplicacao")
async def opMultp(valor_1: int, valor_2: int, oper: str):
    if oper == 'mt'.lower() or '*':
        multiplicacao = (valor_1 * valor_2)
        return multiplicacao


@app.post("/divisao")
async def opDivisao(valor_1: int, valor_2: int, oper: str):
    if oper == 'dv'.lower() or '/':
        divisao = (valor_1 / valor_2)
        return divisao
