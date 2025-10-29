from pydantic import BaseModel
from typing import List, Optional


class Resposta(BaseModel):
    id: int
    conteudo: str


class Questao(BaseModel):
    id: int
    codigo: str
    conteudo: str
    respostas: List[Resposta]


class QuestoesResult(BaseModel):
    questoes: List[Questao]


class QuestionarioRespondido(BaseModel):
    respostas: List[int]


class Tecnica(BaseModel):
    id: int
    codigo: str
    nome: str
    pontuacao: float


class ListaTecnicas(BaseModel):
    tecnicas: List[Tecnica]
