from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
import math
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI (
title =" Calculadora API",
description ="API de Calculadora para Sistemas Distribuidos ",
version =" 1.0.0 ")
# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # libera acesso de qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # permite todos os métodos (GET, POST, OPTIONS etc.)
    allow_headers=["*"],  # permite todos os headers
)

class OperacaoRequest ( BaseModel ) :
    numero1 : float
    numero2 : float

class ResultadoResponse ( BaseModel ) :
    operacao : str
    numero1 : float
    numero2 : float
    resultado : float


@app.get ("/")
def raiz () :
    return {" mensagem ": "Bem - vindo a Calculadora API!", " docs": "/ docs "}



@app.get("/calculadora", response_class=HTMLResponse)
def abrir_frontend():
    with open("interface001.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post ("/somar", response_model = ResultadoResponse )
def somar ( dados : OperacaoRequest ) :
    resultado = dados . numero1 + dados . numero2
    return ResultadoResponse (
    operacao =" soma ",
    numero1 = dados . numero1 ,
    numero2 = dados . numero2 ,
    resultado = resultado)


@app.post ("/subtrair", response_model = ResultadoResponse )
def subtrair ( dados : OperacaoRequest ) :
    resultado = dados.numero1 - dados.numero2
    return ResultadoResponse (
    operacao ="subtracao",
    numero1 = dados.numero1 ,
    numero2 = dados.numero2 ,
    resultado = resultado)

@app . post ("/multiplicar", response_model = ResultadoResponse )
def multiplicar ( dados : OperacaoRequest ) :
    resultado = dados.numero1 * dados.numero2
    return ResultadoResponse (
    operacao ="multiplicacao",
    numero1 = dados.numero1 ,
    numero2 = dados.numero2 ,
    resultado = resultado)



@app.post ("/dividir", response_model = ResultadoResponse )
def dividir ( dados : OperacaoRequest ) :
    if dados.numero2 == 0:
        raise HTTPException (
            status_code=400,
            detail="Divisao por zero nao e permitida!"
        )
    resultado = dados.numero1 / dados.numero2
    return ResultadoResponse (
         operacao =" divisao ",
         numero1 = dados.numero1 ,
         numero2 = dados.numero2 ,
         resultado = resultado
    )


@app.get ("/calcular")
def calcular_query ( numero1 : float , numero2 : float , operacao : str):
    operacoes = {
     "soma": lambda a, b: a + b,
     "subtracao": lambda a, b: a - b,
     "multiplicacao": lambda a, b: a * b,
     "divisao": lambda a, b: a / b,
     "potencia": lambda a, b: a ** b,
     "raiz": lambda a, b: math.sqrt(a)
    }

    if operacao not in operacoes :
        raise HTTPException (
         status_code =400 ,
         detail = f"Operacao invalida.Use: { list ( operacoes.keys())}"
        )
    if operacao == "divisao" and numero2 == 0:
        raise HTTPException ( status_code =400 , detail ="Divisao por zero !")
    return {
         "operacao": operacao ,
         "numero1": numero1 ,
         "numero2": numero2 ,
         "resultado": operacoes [ operacao ]( numero1 , numero2 )
    }


@app.post("/potencia", response_model=ResultadoResponse)
def potencia(dados: OperacaoRequest):
    resultado = dados.numero1 ** dados.numero2
    return ResultadoResponse(
        operacao="potencia",
        numero1=dados.numero1,
        numero2=dados.numero2,
        resultado=resultado
    )

@app.post("/raiz", response_model=ResultadoResponse)
def raiz(dados: OperacaoRequest):
    if dados.numero1 < 0:
        raise HTTPException(
            status_code=400,
            detail="Não é possível calcular raiz quadrada de número negativo!"
        )
    resultado = math.sqrt(dados.numero1)
    return ResultadoResponse(
        operacao="raiz",
        numero1=dados.numero1,
        numero2=dados.numero2,
        resultado=resultado
    )
