from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    cpf: int
    nome: str
    data_nascimento: date

usuarios = [
    {
        'cpf': 10020310231,
        'nome': 'Vitor',
        'data_nascimento': date(2021, 4, 10)
    },
    {
        'cpf': 10020310232,
        'nome': 'Daniel',
        'data_nascimento': date(2021, 4, 12)
    },
    {
        'cpf': 10020310233,
        'nome': 'Lara',
        'data_nascimento': date(2022, 4, 17)
    },
]

@app.get("/")
def home():
    return "API está no ar"

@app.get("/usuarios")
def obter_users():
    return usuarios

@app.post("/usuariospost")
def adicionar_usuario(usuario: Usuario):
    usuarios.append(usuario.dict())
    return {"mensagem": "Usuário adicionado com sucesso"}
