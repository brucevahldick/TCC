from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from .database_models import Tecnica, RespostaFacetaValor, FacetaValor, TecnicaFacetaValor, Questao, Faceta


def get_questoes_e_respostas(db: Session):
    return db.query(Questao).all()


def get_tecnicas_detalhadas(db: Session):
    tecnicas = db.query(Tecnica).all()
    result = []
    for tecnica in tecnicas:
        tecnica_data = {
            "id": tecnica.id,
            "codigo": tecnica.codigo,
            "nome": tecnica.nome,
            "facetas": [],
        }
        for tfv in tecnica.facetas_associadas:
            faceta_valor = tfv.faceta_valor_ref
            faceta = faceta_valor.faceta_ref

            # Busca a pontuação da faceta para a técnica (se houver)
            pontuacao = None
            # A pontuação não está diretamente na TecnicaFacetaValor,
            # mas sim na RespostaFacetaValor.
            # Como este endpoint é para listar todas as técnicas e suas facetas,
            # vamos apenas listar as facetas associadas.

            tecnica_data["facetas"].append({
                "codigo": faceta.codigo,
                "nome": faceta.nome,
                "definicao": faceta.definicao,
                "valor_associado": {
                    "valor": faceta_valor.valor,
                    "pontuacao": None
                }
            })
        result.append(tecnica_data)
    return result


def get_guia_facetado_data(db: Session):
    tecnicas_db = db.query(Tecnica).all()
    tecnicas_data = []
    for tecnica in tecnicas_db:
        tecnica_data = {
            "id": tecnica.id,
            "codigo": tecnica.codigo,
            "nome": tecnica.nome,
            "facetas": [],
        }
        for tfv in tecnica.facetas_associadas:
            faceta_valor = tfv.faceta_valor_ref
            faceta = faceta_valor.faceta_ref

            tecnica_data["facetas"].append({
                "codigo": faceta.codigo,
                "nome": faceta.nome,
                "definicao": faceta.definicao,
                "valor_associado": {
                    "valor": faceta_valor.valor,
                    "pontuacao": None
                }
            })
        tecnicas_data.append(tecnica_data)

    facetas_db = db.query(Faceta).all()
    facetas_data = []
    for faceta in facetas_db:
        facetas_data.append({
            "codigo": faceta.codigo,
            "nome": faceta.nome,
            "definicao": faceta.definicao,
            "valores_possiveis": [fv.valor for fv in faceta.valores if fv.valor is not None]
        })

    return {
        "tecnicas": tecnicas_data,
        "facetas": facetas_data
    }


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
