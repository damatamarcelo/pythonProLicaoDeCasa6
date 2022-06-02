from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"mensagem": "Bem vindo a api para cálculos matemáticos simples."}


class Operacoes(BaseModel):
    valor_1 = int
    valor_2 = int
    oper = str


@app.post("/math")
async def math(opm: Operacoes):
    """
    Esta função executa uma operação matemática simples, conforme abaixo:
    adição = +,
    subtração = -,
    multiplicação = x ou *,
    divisão = / ou :,
    """

    if opm.oper == "+":
        soma = opm.valor_1 + opm.valor_2
        return {"Soma": soma}
    if opm.oper == "-":
        subtracao = (opm.valor_1 - opm.valor_2)
        return {"Subtração": subtracao}
    if opm.oper == "*" or opm.oper == "x".lower():
        multiplicacao = (opm.valor_1 + opm.valor_2)
        return {"Multiplicação": multiplicacao}
    if opm.oper == "/" or opm.oper == ":":
        divisao = (opm.valor_1 - opm.valor_2)
        return {"Divisão": divisao}
    else:
        return {"Mensagem": "Informe um opção válida."}
