from fastapi import APIRouter, HTTPException, status

from application.pessoas_service import PessoasService
from persistence.utils import obter_engine
from presentation.viewmodels.models import *

engine = obter_engine()

router = APIRouter()
prefix = '/pessoas'

pessoas_service = PessoasService()


@router.get('/id_pessoa/{id}', status_code=status.HTTP_200_OK, response_model=PessoasLeitura)
async def obter_pessoas(id: int):
    pessoa = pessoas_service.obter_pessoa_por_id(id)

    if not pessoa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Pessoa não encontrada')
    
    return pessoa


@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_pessoa(pessoa: Pessoas):
    return pessoas_service.criar_pessoa(pessoa)



@router.get('/nomes/{nome}', status_code=status.HTTP_200_OK, response_model=List[PessoasLeitura])
async def buscar_pessoas(nome: str):
    pessoas = pessoas_service.buscar_pessoas(nome)

    if not pessoas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Pessoa não encontrada')
    
    return pessoas

@router.get('/contagem', status_code=status.HTTP_200_OK)
async def contagem_pessoas():
    resultado = pessoas_service.contagem_pessoas()

    return {'Contagem': resultado}