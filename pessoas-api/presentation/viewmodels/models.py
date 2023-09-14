from sqlmodel import Field, SQLModel
from typing import List,Optional


class PessoasBase(SQLModel):
    apelido : str | None = Field(default=None, unique=True, min_length = 1)
    nome: str | None = Field(min_length = 1)
    nascimento : str 
    stack : Optional[List[str]] | None = Field(default=None)

class Pessoas(PessoasBase, table = True):
    id: int | None = Field(default=None, primary_key=True)

class PessoasLeitura(PessoasBase):
    id : int


