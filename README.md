# 📐 Projeto Avaliativo - Calculadora API

**Autores:**
- Wallace Pereira de Castro Souza (ADS 4)  
- Wallison Pereira de Souza Castro (ADS 4)  

**Data:** Abril 2026  

---

## 📌 Resumo
Este projeto foi desenvolvido para a disciplina **Programação de Sistemas Distribuídos** da **Universidade do Grandes Lagos - UNILAGO**, sob supervisão do Professor [Gleydes Oliveira](https://github.com/gleydes).  
Consiste em uma **API de calculadora** implementada em **Python com FastAPI**, integrando operações matemáticas básicas e avançadas, além de uma interface web em HTML.

---

## 🚀 Introdução
O objetivo do projeto é aplicar conceitos de sistemas distribuídos, utilizando o framework **FastAPI** para disponibilizar operações matemáticas como serviços acessíveis via HTTP.  
A solução também inclui uma interface web simples para interação com o usuário.

---

## 🛠️ Estrutura da Solução
A aplicação foi organizada em três componentes principais:

- `main.py`: implementação da API com FastAPI  
- `test_client.py`: versão de teste da API  
- `interface001.html`: interface web para interação com a API  

---

### 📄 Arquivo `main.py`
Configuração inicial da API e definição das rotas:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import math
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Calculadora API",
    description="API de Calculadora para Sistemas Distribuidos",
    version="1.0.0"
)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

📊 Modelos de Dados
python
class OperacaoRequest(BaseModel):
    numero1: float
    numero2: float

class ResultadoResponse(BaseModel):
    operacao: str
    numero1: float
    numero2: float
    resultado: float
Esses modelos garantem a validação dos dados recebidos e enviados pela API.

🔗 Rotas da API
A API disponibiliza rotas para operações matemáticas:

/somar, /subtrair, /multiplicar, /dividir

/potencia, /raiz

/calcular (rota genérica via query string)

Exemplo da rota de soma:

python
@app.post("/somar", response_model=ResultadoResponse)
def somar(dados: OperacaoRequest):
    resultado = dados.numero1 + dados.numero2
    return ResultadoResponse(
        operacao="soma",
        numero1=dados.numero1,
        numero2=dados.numero2,
        resultado=resultado
    )

O arquivo interface001.html fornece uma interface simples para interação com a API:

html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Calculadora API</title>
</head>
<body>
  <h1>Calculadora API</h1>
  <!-- Campos de entrada e seleção de operação -->
  ...
</body>
</html>
O JavaScript integrado envia requisições para a API e exibe o resultado na página.

⚙️ Como Executar
1. Clonar o repositório
bash
git clone https://github.com/Ecallaw312/Projeto-Avaliativo.git
cd Projeto-Avaliativo
2. Instalar dependências
bash
pip install fastapi uvicorn pydantic
3. Executar a API
bash
uvicorn main:app --reload
A API estará disponível em:
👉 http://127.0.0.1:8000

4. Acessar a interface web
Abra o arquivo interface001.html no navegador para interagir com a API.


✅ Conclusão
O projeto demonstra a aplicação prática dos conceitos da disciplina, integrando:

Programação em Python

Validação de dados com Pydantic

Disponibilização de serviços com FastAPI

Interface web em HTML

A solução é modular, extensível e cumpre os requisitos avaliativos.

👨‍🏫 Créditos
Projeto Avaliativo desenvolvido para disciplina Programação de Sistemas Distribuídos da Universidade do Grandes Lagos - UNILAGO, sob supervisão do Professor Gleydes Oliveira.
