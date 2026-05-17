from fastapi import APIRouter #responasavel por criar rotas para a gente
from fastapi.responses import JSONResponse #vai ajudar nós a enviar respostas pelo fast APi

users_routes = APIRouter(tags=["Usuários"])

@users_routes.post("/users")
async def criar_usuario():
    
    return JSONResponse(
        content= {"Olá": "Mundo"},
        status_code=200
    )