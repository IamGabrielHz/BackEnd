from sqlalchemy import  select, func
from sqlmodel import Session,select

from persistence.utils import obter_engine
from presentation.viewmodels.models import *


class PessoasService():

  def __init__(self):
    self.session = Session(obter_engine())

  def obter_pessoa_por_id(self, id: int):
    instrucao = select(Pessoas).where(Pessoas.id == id)
    pessoa = self.session.exec(instrucao).first()
    self.session.close()

    return pessoa
  
  def criar_pessoa(self, pessoa: Pessoas):
    self.session.add(pessoa)
    self.session.commit()
    self.session.refresh(pessoa)
    self.session.close()

    return pessoa
  
  def buscar_pessoas(self,nome: str):
    instrucao = select(Pessoas).where(Pessoas.nome == nome).limit(50)
    pessoas = self.session.exec(instrucao).all()
    self.session.close()

    return pessoas
  
  def contagem_pessoas(self):
    instrucao = select([func.count()]).select_from(Pessoas)
    resultado = self.session.exec(instrucao).one()
    self.session.close()

    return resultado