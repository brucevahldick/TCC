from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

PONTUACAO_MENOR = 0
PONTUACAO_MEDIA = 0.5
PONTUACAO_MAIOR = 1


class Faceta(Base):
    __tablename__ = "facetas"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(50), unique=True, index=True)
    nome = Column(String(100), nullable=False)
    definicao = Column(String(500))
    valores = relationship("FacetaValor", back_populates="faceta_ref")


class FacetaValor(Base):
    __tablename__ = "faceta_valores"
    id = Column(Integer, primary_key=True, index=True)
    faceta_id = Column(Integer, ForeignKey("facetas.id"), nullable=False)
    valor = Column(String(100), nullable=True)
    faceta_ref = relationship("Faceta", back_populates="valores")
    respostas_associadas = relationship("RespostaFacetaValor", back_populates="faceta_valor_ref")


class Tecnica(Base):
    __tablename__ = "tecnicas"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(50), unique=True, index=True)
    nome = Column(String(100), nullable=False)
    facetas_associadas = relationship("TecnicaFacetaValor", back_populates="tecnica_ref")


class TecnicaFacetaValor(Base):
    __tablename__ = "tecnica_faceta_valores"
    tecnica_id = Column(Integer, ForeignKey("tecnicas.id"), primary_key=True)
    faceta_valor_id = Column(Integer, ForeignKey("faceta_valores.id"), primary_key=True)
    tecnica_ref = relationship("Tecnica", back_populates="facetas_associadas")
    faceta_valor_ref = relationship("FacetaValor")


class Questao(Base):
    __tablename__ = "questoes"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(50), unique=True, index=True)
    conteudo = Column(String(500), nullable=False)
    respostas = relationship("Resposta", back_populates="questao_ref")


class Resposta(Base):
    __tablename__ = "respostas"
    id = Column(Integer, primary_key=True, index=True)
    questao_id = Column(Integer, ForeignKey("questoes.id"), nullable=False)
    conteudo = Column(String(100), index=True)
    questao_ref = relationship("Questao", back_populates="respostas")
    facetas_associadas = relationship("RespostaFacetaValor", back_populates="resposta_ref")


class RespostaFacetaValor(Base):
    __tablename__ = "resposta_faceta_valores"
    resposta_id = Column(Integer, ForeignKey("respostas.id"), primary_key=True)
    faceta_valor_id = Column(Integer, ForeignKey("faceta_valores.id"), primary_key=True)
    pontuacao = Column(Float, nullable=False)
    resposta_ref = relationship("Resposta", back_populates="facetas_associadas")
    faceta_valor_ref = relationship("FacetaValor", back_populates="respostas_associadas")
