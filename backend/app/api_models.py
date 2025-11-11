from pydantic import BaseModel
from typing import List, Optional, Dict, Any


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


class FacetaValorDetalhe(BaseModel):
    valor: Optional[str]
    pontuacao: Optional[float]

class FacetaDetalhe(BaseModel):
    codigo: str
    nome: str
    definicao: Optional[str]
    valor_associado: FacetaValorDetalhe

class TecnicaDetalhada(BaseModel):
    id: int
    codigo: str
    nome: str
    facetas: List[FacetaDetalhe]

class Tecnica(BaseModel):
    id: int
    codigo: str
    nome: str
    pontuacao: float


class ListaTecnicas(BaseModel):
    tecnicas: List[Tecnica]

class ListaTecnicasDetalhada(BaseModel):
    tecnicas: List[TecnicaDetalhada]
