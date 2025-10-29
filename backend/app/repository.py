from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from .database_models import Tecnica, RespostaFacetaValor, FacetaValor, TecnicaFacetaValor, Questao


def get_questoes_e_respostas(db: Session):
    return db.query(Questao).all()


def calcula_recomendacao(db: Session, resposta_ids: list[int]):
    query = (
        db.query(
            func.sum(RespostaFacetaValor.pontuacao).label("soma_pontuacao"),
            Tecnica.id.label("tecnica_id"),
            Tecnica.codigo.label("tecnica_codigo"),
            Tecnica.nome.label("tecnica_nome"),
        )
        .join(FacetaValor, FacetaValor.id == RespostaFacetaValor.faceta_valor_id)
        .join(TecnicaFacetaValor, TecnicaFacetaValor.faceta_valor_id == FacetaValor.id)
        .join(Tecnica, Tecnica.id == TecnicaFacetaValor.tecnica_id)
        .filter(RespostaFacetaValor.resposta_id.in_(resposta_ids))
        .group_by(Tecnica.id, Tecnica.codigo, Tecnica.nome)
        .order_by(desc("soma_pontuacao"))
    )

    results = query.all()

    return [
        {
            "id": tecnica_id,
            "codigo": tecnica_codigo,
            "nome": tecnica_nome,
            "pontuacao": soma_pontuacao,
        }
        for soma_pontuacao, tecnica_id, tecnica_codigo, tecnica_nome in results
    ]
