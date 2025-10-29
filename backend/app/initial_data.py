import sys
import os
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .database import engine, Base, SessionLocal
from .database_models import (
    Faceta, FacetaValor, Tecnica, TecnicaFacetaValor,
    Questao, Resposta, RespostaFacetaValor
)


def create_initial_data(db: Session):
    """
    Cria dados iniciais (seed) na base de dados.
    """
    print("--- A INSERIR DADOS INICIAIS ---")

    try:
        # 1. FACETAS
        faceta_f1 = Faceta(codigo="F1", nome="Grau de Formalidade",
                           definicao="Representa o nível de rigor sintático e semântico da técnica, indicando o quanto ela permite ambiguidades.")
        faceta_f2 = Faceta(codigo="F2", nome="Intuitividade para Usuários de Negócio",
                           definicao="Mede o quão compreensível a técnica é para usuários sem formação técnica.")
        faceta_f3 = Faceta(codigo="F3", nome="Base para Projeto e Teste",
                           definicao="Indica se a técnica fornece uma base clara e verificável para desenvolvimento e teste.")
        faceta_f4 = Faceta(codigo="F4", nome="Verificação Automatizada",
                           definicao="Define a possibilidade de verificação automática de consistência, erros estruturais e comportamentais.")
        faceta_f5 = Faceta(codigo="F5", nome="Foco no Comportamento Observável",
                           definicao="Representa o foco da técnica no comportamento observável - interface e estímulo-resposta - em vez da estrutura interna.")
        faceta_f6 = Faceta(codigo="F6", nome="Assistência Organizacional do Documento de Requisitos",
                           definicao="Mede o quanto a técnica ajuda a estruturar, hierarquizar e organizar os requisitos documentados.")
        faceta_f7 = Faceta(codigo="F7", nome="Suporte à Geração de Protótipos/Testes",
                           definicao="Indica se há ferramentas ou meios de gerar protótipos ou testes a partir das especificações.")
        faceta_f8 = Faceta(codigo="F8", nome="Tipo de Aplicação Adequado",
                           definicao="Define o contexto de aplicação mais apropriado.")
        faceta_f9 = Faceta(codigo="F9", nome="Expressividade Visual",
                           definicao="Refere-se ao uso de diagramas e representações gráficas como suporte cognitivo.")
        faceta_f10 = Faceta(codigo="F10", nome="Integração com Métodos Ágeis",
                            definicao="Avalia o nível de compatibilidade da técnica com práticas e princípios ágeis.")
        faceta_f11 = Faceta(codigo="F11", nome="Dificuldade de Adoção / Treinamento Necessário",
                            definicao="Representa o grau de complexidade de aprendizado e necessidade de treinamento formal.")

        db.add_all([
            faceta_f1, faceta_f2, faceta_f3, faceta_f4, faceta_f5,
            faceta_f6, faceta_f7, faceta_f8, faceta_f9, faceta_f10, faceta_f11
        ])
        db.commit()

        # 2. VALORES DE FACETAS
        valor_faceta_f1_1 = FacetaValor(faceta_id=faceta_f1.id, valor="Formal")
        valor_faceta_f1_2 = FacetaValor(faceta_id=faceta_f1.id, valor="Semi-formal")
        valor_faceta_f1_3 = FacetaValor(faceta_id=faceta_f1.id, valor="Informal")

        valor_faceta_f2_1 = FacetaValor(faceta_id=faceta_f2.id, valor="Alta")
        valor_faceta_f2_2 = FacetaValor(faceta_id=faceta_f2.id, valor="Média")
        valor_faceta_f2_3 = FacetaValor(faceta_id=faceta_f2.id, valor="Baixa")

        valor_faceta_f3_1 = FacetaValor(faceta_id=faceta_f3.id, valor="Ausente")
        valor_faceta_f3_2 = FacetaValor(faceta_id=faceta_f3.id, valor="Parcial")
        valor_faceta_f3_3 = FacetaValor(faceta_id=faceta_f3.id, valor="Presente")

        valor_faceta_f4_1 = FacetaValor(faceta_id=faceta_f4.id, valor="Inexistente")
        valor_faceta_f4_2 = FacetaValor(faceta_id=faceta_f4.id, valor="Parcial")
        valor_faceta_f4_3 = FacetaValor(faceta_id=faceta_f4.id, valor="Completa")

        valor_faceta_f5_1 = FacetaValor(faceta_id=faceta_f5.id, valor="Baixa")
        valor_faceta_f5_2 = FacetaValor(faceta_id=faceta_f5.id, valor="Média")
        valor_faceta_f5_3 = FacetaValor(faceta_id=faceta_f5.id, valor="Alta")

        valor_faceta_f6_1 = FacetaValor(faceta_id=faceta_f6.id, valor="Baixa")
        valor_faceta_f6_2 = FacetaValor(faceta_id=faceta_f6.id, valor="Média")
        valor_faceta_f6_3 = FacetaValor(faceta_id=faceta_f6.id, valor="Alta")

        valor_faceta_f7_1 = FacetaValor(faceta_id=faceta_f7.id, valor="Nenhum")
        valor_faceta_f7_2 = FacetaValor(faceta_id=faceta_f7.id, valor="Protótipos")
        valor_faceta_f7_3 = FacetaValor(faceta_id=faceta_f7.id, valor="Testes Automáticos")

        valor_faceta_f8_1 = FacetaValor(faceta_id=faceta_f8.id, valor="Geral")
        valor_faceta_f8_2 = FacetaValor(faceta_id=faceta_f8.id, valor="Sistemas de negócio")
        valor_faceta_f8_3 = FacetaValor(faceta_id=faceta_f8.id, valor="Sistemas em tempo real")

        valor_faceta_f9_1 = FacetaValor(faceta_id=faceta_f9.id, valor="Textual")
        valor_faceta_f9_2 = FacetaValor(faceta_id=faceta_f9.id, valor="Gráfica")

        valor_faceta_f10_1 = FacetaValor(faceta_id=faceta_f10.id, valor="Alta")
        valor_faceta_f10_2 = FacetaValor(faceta_id=faceta_f10.id, valor="Média")
        valor_faceta_f10_3 = FacetaValor(faceta_id=faceta_f10.id, valor="Baixa")

        valor_faceta_f11_1 = FacetaValor(faceta_id=faceta_f11.id, valor="Baixa")
        valor_faceta_f11_2 = FacetaValor(faceta_id=faceta_f11.id, valor="Média")
        valor_faceta_f11_3 = FacetaValor(faceta_id=faceta_f11.id, valor="Alta")

        db.add_all([
            valor_faceta_f1_1, valor_faceta_f1_2, valor_faceta_f1_3,
            valor_faceta_f2_1, valor_faceta_f2_2, valor_faceta_f2_3,
            valor_faceta_f3_1, valor_faceta_f3_2, valor_faceta_f3_3,
            valor_faceta_f4_1, valor_faceta_f4_2, valor_faceta_f4_3,
            valor_faceta_f5_1, valor_faceta_f5_2, valor_faceta_f5_3,
            valor_faceta_f6_1, valor_faceta_f6_2, valor_faceta_f6_3,
            valor_faceta_f7_1, valor_faceta_f7_2, valor_faceta_f7_3,
            valor_faceta_f8_1, valor_faceta_f8_2, valor_faceta_f8_3,
            valor_faceta_f9_1, valor_faceta_f9_2,
            valor_faceta_f10_1, valor_faceta_f10_2, valor_faceta_f10_3,
            valor_faceta_f11_1, valor_faceta_f11_2, valor_faceta_f11_3
        ])
        db.commit()

        # 3. TÉCNICAS
        tecnica_t1 = Tecnica(codigo="T1", nome="Linguagem Natural")
        tecnica_t2 = Tecnica(codigo="T2", nome="Máquina de Estados Finitos")
        tecnica_t3 = Tecnica(codigo="T3", nome="Tabelas de Decisão e Árvores de Decisão")
        tecnica_t4 = Tecnica(codigo="T4", nome="Program Design Language (PDL)")
        tecnica_t5 = Tecnica(codigo="T5", nome="Structured Analysis/Real-Time (SA/RT)")
        tecnica_t6 = Tecnica(codigo="T6", nome="Statecharts")
        tecnica_t7 = Tecnica(codigo="T7", nome="Requirements Engineering Validation System (REVS)")
        tecnica_t8 = Tecnica(codigo="T8", nome="Requirements Language Processor (RLP)")
        tecnica_t9 = Tecnica(codigo="T9", nome="The Specification and Description Language (SDL)")
        tecnica_t10 = Tecnica(codigo="T10", nome="PAISLey")
        tecnica_t11 = Tecnica(codigo="T11", nome="Petri-nets")
        tecnica_t12 = Tecnica(codigo="T12", nome="UML")
        tecnica_t13 = Tecnica(codigo="T13", nome="Business Process Model and Notation (BPMN)")
        tecnica_t14 = Tecnica(codigo="T14", nome="Event-drive Process Chains (EPC)")
        tecnica_t15 = Tecnica(codigo="T15", nome="User Stories")

        db.add_all([
            tecnica_t1,
            tecnica_t2,
            tecnica_t3,
            tecnica_t4,
            tecnica_t5,
            tecnica_t6,
            tecnica_t7,
            tecnica_t8,
            tecnica_t9,
            tecnica_t10,
            tecnica_t11,
            tecnica_t12,
            tecnica_t13,
            tecnica_t14,
            tecnica_t15
        ])
        db.commit()

        # 4. ASSOCIAÇÃO TÉCNICA-FACETA (Exemplo: Brainstorming é Baixa Complexidade e Curto Tempo)

        # T1 – Linguagem Natural
        tf1_1 = TecnicaFacetaValor(tecnica_id=tecnica_t1.id, faceta_valor_id=valor_faceta_f1_3.id)  # F1 (Informal)
        tf1_2 = TecnicaFacetaValor(tecnica_id=tecnica_t1.id, faceta_valor_id=valor_faceta_f2_1.id)  # F2 (Alta)
        tf1_3 = TecnicaFacetaValor(tecnica_id=tecnica_t1.id, faceta_valor_id=valor_faceta_f3_1.id)  # F3 (Ausente)
        tf1_4 = TecnicaFacetaValor(tecnica_id=tecnica_t1.id, faceta_valor_id=valor_faceta_f4_1.id)  # F4 (Inexistente)
        tf1_5 = TecnicaFacetaValor(tecnica_id=tecnica_t1.id, faceta_valor_id=valor_faceta_f5_1.id)  # F5 (Baixa)
        tf1_6 = TecnicaFacetaValor(tecnica_id=tecnica_t1.id, faceta_valor_id=valor_faceta_f6_1.id)  # F6 (Baixa)
        tf1_7 = TecnicaFacetaValor(tecnica_id=tecnica_t1.id, faceta_valor_id=valor_faceta_f7_1.id)  # F7 (Nenhum)
        tf1_8 = TecnicaFacetaValor(tecnica_id=tecnica_t1.id, faceta_valor_id=valor_faceta_f8_1.id)  # F8 (Geral)
        tf1_9 = TecnicaFacetaValor(tecnica_id=tecnica_t1.id, faceta_valor_id=valor_faceta_f9_1.id)  # F9 (Textual)
        tf1_10 = TecnicaFacetaValor(tecnica_id=tecnica_t1.id, faceta_valor_id=valor_faceta_f10_1.id)  # F10 (Alta)
        tf1_11 = TecnicaFacetaValor(tecnica_id=tecnica_t1.id, faceta_valor_id=valor_faceta_f11_1.id)  # F11 (Baixa)
        db.add_all([tf1_1, tf1_2, tf1_3, tf1_4, tf1_5, tf1_6, tf1_7, tf1_8, tf1_9, tf1_10, tf1_11])
        db.commit()

        # T2 – Máquina de Estados Finitos
        tf2_1 = TecnicaFacetaValor(tecnica_id=tecnica_t2.id, faceta_valor_id=valor_faceta_f1_1.id)  # F1 (Formal)
        tf2_2 = TecnicaFacetaValor(tecnica_id=tecnica_t2.id, faceta_valor_id=valor_faceta_f2_2.id)  # F2 (Média)
        tf2_3 = TecnicaFacetaValor(tecnica_id=tecnica_t2.id, faceta_valor_id=valor_faceta_f3_3.id)  # F3 (Presente)
        tf2_4 = TecnicaFacetaValor(tecnica_id=tecnica_t2.id, faceta_valor_id=valor_faceta_f4_3.id)  # F4 (Completa)
        tf2_5 = TecnicaFacetaValor(tecnica_id=tecnica_t2.id, faceta_valor_id=valor_faceta_f5_2.id)  # F5 (Média)
        tf2_6 = TecnicaFacetaValor(tecnica_id=tecnica_t2.id, faceta_valor_id=valor_faceta_f6_2.id)  # F6 (Média)
        tf2_7 = TecnicaFacetaValor(tecnica_id=tecnica_t2.id, faceta_valor_id=valor_faceta_f7_2.id)  # F7 (Protótipos)
        tf2_8 = TecnicaFacetaValor(tecnica_id=tecnica_t2.id, faceta_valor_id=valor_faceta_f8_3.id)  # F8 (Tempo Real)
        tf2_9 = TecnicaFacetaValor(tecnica_id=tecnica_t2.id, faceta_valor_id=valor_faceta_f9_2.id)  # F9 (Gráfica)
        tf2_10 = TecnicaFacetaValor(tecnica_id=tecnica_t2.id, faceta_valor_id=valor_faceta_f10_3.id)  # F10 (Baixa)
        tf2_11 = TecnicaFacetaValor(tecnica_id=tecnica_t2.id, faceta_valor_id=valor_faceta_f11_2.id)  # F11 (Média)
        db.add_all([tf2_1, tf2_2, tf2_3, tf2_4, tf2_5, tf2_6, tf2_7, tf2_8, tf2_9, tf2_10, tf2_11])
        db.commit()

        # T3 – Tabelas/Árvores de Decisão
        tf3_1 = TecnicaFacetaValor(tecnica_id=tecnica_t3.id, faceta_valor_id=valor_faceta_f1_2.id)  # F1 (Semi-formal)
        tf3_2 = TecnicaFacetaValor(tecnica_id=tecnica_t3.id, faceta_valor_id=valor_faceta_f2_1.id)  # F2 (Alta)
        tf3_3 = TecnicaFacetaValor(tecnica_id=tecnica_t3.id, faceta_valor_id=valor_faceta_f3_2.id)  # F3 (Parcial)
        tf3_4 = TecnicaFacetaValor(tecnica_id=tecnica_t3.id, faceta_valor_id=valor_faceta_f4_1.id)  # F4 (Inexistente)
        tf3_5 = TecnicaFacetaValor(tecnica_id=tecnica_t3.id, faceta_valor_id=valor_faceta_f5_2.id)  # F5 (Média)
        tf3_6 = TecnicaFacetaValor(tecnica_id=tecnica_t3.id, faceta_valor_id=valor_faceta_f6_2.id)  # F6 (Média)
        tf3_7 = TecnicaFacetaValor(tecnica_id=tecnica_t3.id, faceta_valor_id=valor_faceta_f7_1.id)  # F7 (Nenhum)
        tf3_8 = TecnicaFacetaValor(tecnica_id=tecnica_t3.id, faceta_valor_id=valor_faceta_f8_1.id)  # F8 (Geral)
        tf3_9 = TecnicaFacetaValor(tecnica_id=tecnica_t3.id, faceta_valor_id=valor_faceta_f9_1.id)  # F9 (Textual)
        tf3_10 = TecnicaFacetaValor(tecnica_id=tecnica_t3.id, faceta_valor_id=valor_faceta_f10_3.id)  # F10 (Baixa)
        tf3_11 = TecnicaFacetaValor(tecnica_id=tecnica_t3.id, faceta_valor_id=valor_faceta_f11_1.id)  # F11 (Baixa)
        db.add_all([tf3_1, tf3_2, tf3_3, tf3_4, tf3_5, tf3_6, tf3_7, tf3_8, tf3_9, tf3_10, tf3_11])
        db.commit()

        # T4 – PDL (Program Design Language)
        tf4_1 = TecnicaFacetaValor(tecnica_id=tecnica_t4.id, faceta_valor_id=valor_faceta_f1_3.id)  # F1 (Informal)
        tf4_2 = TecnicaFacetaValor(tecnica_id=tecnica_t4.id, faceta_valor_id=valor_faceta_f2_1.id)  # F2 (Alta)
        tf4_3 = TecnicaFacetaValor(tecnica_id=tecnica_t4.id, faceta_valor_id=valor_faceta_f3_2.id)  # F3 (Parcial)
        tf4_4 = TecnicaFacetaValor(tecnica_id=tecnica_t4.id, faceta_valor_id=valor_faceta_f4_2.id)  # F4 (Parcial)
        tf4_5 = TecnicaFacetaValor(tecnica_id=tecnica_t4.id, faceta_valor_id=valor_faceta_f5_1.id)  # F5 (Baixa)
        tf4_6 = TecnicaFacetaValor(tecnica_id=tecnica_t4.id, faceta_valor_id=valor_faceta_f6_1.id)  # F6 (Baixa)
        tf4_7 = TecnicaFacetaValor(tecnica_id=tecnica_t4.id, faceta_valor_id=valor_faceta_f7_1.id)  # F7 (Nenhum)
        tf4_8 = TecnicaFacetaValor(tecnica_id=tecnica_t4.id, faceta_valor_id=valor_faceta_f8_1.id)  # F8 (Geral)
        tf4_9 = TecnicaFacetaValor(tecnica_id=tecnica_t4.id, faceta_valor_id=valor_faceta_f9_1.id)  # F9 (Textual)
        tf4_10 = TecnicaFacetaValor(tecnica_id=tecnica_t4.id, faceta_valor_id=valor_faceta_f10_3.id)  # F10 (Baixa)
        tf4_11 = TecnicaFacetaValor(tecnica_id=tecnica_t4.id, faceta_valor_id=valor_faceta_f11_1.id)  # F11 (Baixa)
        db.add_all([tf4_1, tf4_2, tf4_3, tf4_4, tf4_5, tf4_6, tf4_7, tf4_8, tf4_9, tf4_10, tf4_11])
        db.commit()

        # T5 – SA/RT (Structured Analysis/Real-Time)
        tf5_1 = TecnicaFacetaValor(tecnica_id=tecnica_t5.id, faceta_valor_id=valor_faceta_f1_2.id)  # F1 (Semi-formal)
        tf5_2 = TecnicaFacetaValor(tecnica_id=tecnica_t5.id, faceta_valor_id=valor_faceta_f2_2.id)  # F2 (Média)
        tf5_3 = TecnicaFacetaValor(tecnica_id=tecnica_t5.id, faceta_valor_id=valor_faceta_f3_3.id)  # F3 (Presente)
        tf5_4 = TecnicaFacetaValor(tecnica_id=tecnica_t5.id, faceta_valor_id=valor_faceta_f4_2.id)  # F4 (Parcial)
        tf5_5 = TecnicaFacetaValor(tecnica_id=tecnica_t5.id, faceta_valor_id=valor_faceta_f5_2.id)  # F5 (Média)
        tf5_6 = TecnicaFacetaValor(tecnica_id=tecnica_t5.id, faceta_valor_id=valor_faceta_f6_2.id)  # F6 (Média)
        tf5_7 = TecnicaFacetaValor(tecnica_id=tecnica_t5.id, faceta_valor_id=valor_faceta_f7_1.id)  # F7 (Nenhum)
        tf5_8 = TecnicaFacetaValor(tecnica_id=tecnica_t5.id, faceta_valor_id=valor_faceta_f8_1.id)  # F8 (Geral)
        tf5_9 = TecnicaFacetaValor(tecnica_id=tecnica_t5.id, faceta_valor_id=valor_faceta_f9_2.id)  # F9 (Gráfica)
        tf5_10 = TecnicaFacetaValor(tecnica_id=tecnica_t5.id, faceta_valor_id=valor_faceta_f10_3.id)  # F10 (Baixa)
        tf5_11 = TecnicaFacetaValor(tecnica_id=tecnica_t5.id, faceta_valor_id=valor_faceta_f11_2.id)  # F11 (Média)
        db.add_all([tf5_1, tf5_2, tf5_3, tf5_4, tf5_5, tf5_6, tf5_7, tf5_8, tf5_9, tf5_10, tf5_11])
        db.commit()

        # T6 – Statecharts
        tf6_1 = TecnicaFacetaValor(tecnica_id=tecnica_t6.id, faceta_valor_id=valor_faceta_f1_1.id)  # F1 (Formal)
        tf6_2 = TecnicaFacetaValor(tecnica_id=tecnica_t6.id, faceta_valor_id=valor_faceta_f2_2.id)  # F2 (Média)
        tf6_3 = TecnicaFacetaValor(tecnica_id=tecnica_t6.id, faceta_valor_id=valor_faceta_f3_3.id)  # F3 (Presente)
        tf6_4 = TecnicaFacetaValor(tecnica_id=tecnica_t6.id, faceta_valor_id=valor_faceta_f4_3.id)  # F4 (Completa)
        tf6_5 = TecnicaFacetaValor(tecnica_id=tecnica_t6.id, faceta_valor_id=valor_faceta_f5_2.id)  # F5 (Média)
        tf6_6 = TecnicaFacetaValor(tecnica_id=tecnica_t6.id, faceta_valor_id=valor_faceta_f6_3.id)  # F6 (Alta)
        tf6_7 = TecnicaFacetaValor(tecnica_id=tecnica_t6.id, faceta_valor_id=valor_faceta_f7_2.id)  # F7 (Protótipos)
        tf6_8 = TecnicaFacetaValor(tecnica_id=tecnica_t6.id, faceta_valor_id=valor_faceta_f8_3.id)  # F8 (Tempo Real)
        tf6_9 = TecnicaFacetaValor(tecnica_id=tecnica_t6.id, faceta_valor_id=valor_faceta_f9_2.id)  # F9 (Gráfica)
        tf6_10 = TecnicaFacetaValor(tecnica_id=tecnica_t6.id, faceta_valor_id=valor_faceta_f10_3.id)  # F10 (Baixa)
        tf6_11 = TecnicaFacetaValor(tecnica_id=tecnica_t6.id, faceta_valor_id=valor_faceta_f11_3.id)  # F11 (Alta)
        db.add_all([tf6_1, tf6_2, tf6_3, tf6_4, tf6_5, tf6_6, tf6_7, tf6_8, tf6_9, tf6_10, tf6_11])
        db.commit()

        # T7 – REVS
        tf7_1 = TecnicaFacetaValor(tecnica_id=tecnica_t7.id, faceta_valor_id=valor_faceta_f1_1.id)  # F1 (Formal)
        tf7_2 = TecnicaFacetaValor(tecnica_id=tecnica_t7.id, faceta_valor_id=valor_faceta_f2_2.id)  # F2 (Média)
        tf7_3 = TecnicaFacetaValor(tecnica_id=tecnica_t7.id, faceta_valor_id=valor_faceta_f3_3.id)  # F3 (Presente)
        tf7_4 = TecnicaFacetaValor(tecnica_id=tecnica_t7.id, faceta_valor_id=valor_faceta_f4_3.id)  # F4 (Completa)
        tf7_5 = TecnicaFacetaValor(tecnica_id=tecnica_t7.id, faceta_valor_id=valor_faceta_f5_3.id)  # F5 (Alta)
        tf7_6 = TecnicaFacetaValor(tecnica_id=tecnica_t7.id, faceta_valor_id=valor_faceta_f6_3.id)  # F6 (Alta)
        tf7_7 = TecnicaFacetaValor(tecnica_id=tecnica_t7.id, faceta_valor_id=valor_faceta_f7_2.id)  # F7 (Protótipos)
        tf7_8 = TecnicaFacetaValor(tecnica_id=tecnica_t7.id, faceta_valor_id=valor_faceta_f8_3.id)  # F8 (Tempo Real)
        tf7_9 = TecnicaFacetaValor(tecnica_id=tecnica_t7.id, faceta_valor_id=valor_faceta_f9_2.id)  # F9 (Gráfica)
        tf7_10 = TecnicaFacetaValor(tecnica_id=tecnica_t7.id, faceta_valor_id=valor_faceta_f10_3.id)  # F10 (Baixa)
        tf7_11 = TecnicaFacetaValor(tecnica_id=tecnica_t7.id, faceta_valor_id=valor_faceta_f11_3.id)  # F11 (Alta)
        db.add_all([tf7_1, tf7_2, tf7_3, tf7_4, tf7_5, tf7_6, tf7_7, tf7_8, tf7_9, tf7_10, tf7_11])
        db.commit()

        # T8 – RLP
        tf8_1 = TecnicaFacetaValor(tecnica_id=tecnica_t8.id, faceta_valor_id=valor_faceta_f1_1.id)  # F1 (Formal)
        tf8_2 = TecnicaFacetaValor(tecnica_id=tecnica_t8.id, faceta_valor_id=valor_faceta_f2_2.id)  # F2 (Média)
        tf8_3 = TecnicaFacetaValor(tecnica_id=tecnica_t8.id, faceta_valor_id=valor_faceta_f3_3.id)  # F3 (Presente)
        tf8_4 = TecnicaFacetaValor(tecnica_id=tecnica_t8.id, faceta_valor_id=valor_faceta_f4_3.id)  # F4 (Completa)
        tf8_5 = TecnicaFacetaValor(tecnica_id=tecnica_t8.id, faceta_valor_id=valor_faceta_f5_3.id)  # F5 (Alta)
        tf8_6 = TecnicaFacetaValor(tecnica_id=tecnica_t8.id, faceta_valor_id=valor_faceta_f6_3.id)  # F6 (Alta)
        tf8_7 = TecnicaFacetaValor(tecnica_id=tecnica_t8.id,
                                   faceta_valor_id=valor_faceta_f7_3.id)  # F7 (Testes Automáticos)
        tf8_8 = TecnicaFacetaValor(tecnica_id=tecnica_t8.id, faceta_valor_id=valor_faceta_f8_3.id)  # F8 (Tempo Real)
        tf8_9 = TecnicaFacetaValor(tecnica_id=tecnica_t8.id, faceta_valor_id=valor_faceta_f9_1.id)  # F9 (Textual)
        tf8_10 = TecnicaFacetaValor(tecnica_id=tecnica_t8.id, faceta_valor_id=valor_faceta_f10_3.id)  # F10 (Baixa)
        tf8_11 = TecnicaFacetaValor(tecnica_id=tecnica_t8.id, faceta_valor_id=valor_faceta_f11_3.id)  # F11 (Alta)
        db.add_all([tf8_1, tf8_2, tf8_3, tf8_4, tf8_5, tf8_6, tf8_7, tf8_8, tf8_9, tf8_10, tf8_8])
        db.commit()

        # T9 – SDL
        tf9_1 = TecnicaFacetaValor(tecnica_id=tecnica_t9.id, faceta_valor_id=valor_faceta_f1_1.id)  # F1 (Formal)
        tf9_2 = TecnicaFacetaValor(tecnica_id=tecnica_t9.id, faceta_valor_id=valor_faceta_f2_3.id)  # F2 (Baixa)
        tf9_3 = TecnicaFacetaValor(tecnica_id=tecnica_t9.id, faceta_valor_id=valor_faceta_f3_3.id)  # F3 (Presente)
        tf9_4 = TecnicaFacetaValor(tecnica_id=tecnica_t9.id, faceta_valor_id=valor_faceta_f4_3.id)  # F4 (Completa)
        tf9_5 = TecnicaFacetaValor(tecnica_id=tecnica_t9.id, faceta_valor_id=valor_faceta_f5_3.id)  # F5 (Alta)
        tf9_6 = TecnicaFacetaValor(tecnica_id=tecnica_t9.id, faceta_valor_id=valor_faceta_f6_3.id)  # F6 (Alta)
        tf9_7 = TecnicaFacetaValor(tecnica_id=tecnica_t9.id, faceta_valor_id=valor_faceta_f7_2.id)  # F7 (Protótipos)
        tf9_8 = TecnicaFacetaValor(tecnica_id=tecnica_t9.id, faceta_valor_id=valor_faceta_f8_3.id)  # F8 (Tempo Real)
        tf9_9 = TecnicaFacetaValor(tecnica_id=tecnica_t9.id, faceta_valor_id=valor_faceta_f9_2.id)  # F9 (Gráfica)
        tf9_10 = TecnicaFacetaValor(tecnica_id=tecnica_t9.id, faceta_valor_id=valor_faceta_f10_3.id)  # F10 (Baixa)
        tf9_11 = TecnicaFacetaValor(tecnica_id=tecnica_t9.id, faceta_valor_id=valor_faceta_f11_3.id)  # F11 (Alta)
        db.add_all([tf9_1, tf9_2, tf9_3, tf9_4, tf9_5, tf9_6, tf9_7, tf9_8, tf9_9, tf9_10, tf9_11])
        db.commit()

        # T10 – PAISLey
        tf10_1 = TecnicaFacetaValor(tecnica_id=tecnica_t10.id, faceta_valor_id=valor_faceta_f1_1.id)  # F1 (Formal)
        tf10_2 = TecnicaFacetaValor(tecnica_id=tecnica_t10.id, faceta_valor_id=valor_faceta_f2_3.id)  # F2 (Baixa)
        tf10_3 = TecnicaFacetaValor(tecnica_id=tecnica_t10.id, faceta_valor_id=valor_faceta_f3_3.id)  # F3 (Presente)
        tf10_4 = TecnicaFacetaValor(tecnica_id=tecnica_t10.id, faceta_valor_id=valor_faceta_f4_3.id)  # F4 (Completa)
        tf10_5 = TecnicaFacetaValor(tecnica_id=tecnica_t10.id, faceta_valor_id=valor_faceta_f5_2.id)  # F5 (Média)
        tf10_6 = TecnicaFacetaValor(tecnica_id=tecnica_t10.id, faceta_valor_id=valor_faceta_f6_3.id)  # F6 (Alta)
        tf10_7 = TecnicaFacetaValor(tecnica_id=tecnica_t10.id, faceta_valor_id=valor_faceta_f7_2.id)  # F7 (Protótipos)
        tf10_8 = TecnicaFacetaValor(tecnica_id=tecnica_t10.id, faceta_valor_id=valor_faceta_f8_3.id)  # F8 (Tempo Real)
        tf10_9 = TecnicaFacetaValor(tecnica_id=tecnica_t10.id, faceta_valor_id=valor_faceta_f9_1.id)  # F9 (Textual)
        tf10_10 = TecnicaFacetaValor(tecnica_id=tecnica_t10.id, faceta_valor_id=valor_faceta_f10_3.id)  # F10 (Baixa)
        tf10_11 = TecnicaFacetaValor(tecnica_id=tecnica_t10.id, faceta_valor_id=valor_faceta_f11_3.id)  # F11 (Alta)
        db.add_all([tf10_1, tf10_2, tf10_3, tf10_4, tf10_5, tf10_6, tf10_7, tf10_8, tf10_9, tf10_10, tf10_11])
        db.commit()

        # T11 – Petri-nets
        tf11_1 = TecnicaFacetaValor(tecnica_id=tecnica_t11.id, faceta_valor_id=valor_faceta_f1_1.id)  # F1 (Formal)
        tf11_2 = TecnicaFacetaValor(tecnica_id=tecnica_t11.id, faceta_valor_id=valor_faceta_f2_3.id)  # F2 (Baixa)
        tf11_3 = TecnicaFacetaValor(tecnica_id=tecnica_t11.id, faceta_valor_id=valor_faceta_f3_3.id)  # F3 (Presente)
        tf11_4 = TecnicaFacetaValor(tecnica_id=tecnica_t11.id, faceta_valor_id=valor_faceta_f4_2.id)  # F4 (Parcial)
        tf11_5 = TecnicaFacetaValor(tecnica_id=tecnica_t11.id, faceta_valor_id=valor_faceta_f5_2.id)  # F5 (Média)
        tf11_6 = TecnicaFacetaValor(tecnica_id=tecnica_t11.id, faceta_valor_id=valor_faceta_f6_2.id)  # F6 (Média)
        tf11_7 = TecnicaFacetaValor(tecnica_id=tecnica_t11.id, faceta_valor_id=valor_faceta_f7_1.id)  # F7 (Nenhum)
        tf11_8 = TecnicaFacetaValor(tecnica_id=tecnica_t11.id, faceta_valor_id=valor_faceta_f8_3.id)  # F8 (Tempo Real)
        tf11_9 = TecnicaFacetaValor(tecnica_id=tecnica_t11.id, faceta_valor_id=valor_faceta_f9_2.id)  # F9 (Gráfica)
        tf11_10 = TecnicaFacetaValor(tecnica_id=tecnica_t11.id, faceta_valor_id=valor_faceta_f10_3.id)  # F10 (Baixa)
        tf11_11 = TecnicaFacetaValor(tecnica_id=tecnica_t11.id, faceta_valor_id=valor_faceta_f11_3.id)  # F11 (Alta)
        db.add_all([tf11_1, tf11_2, tf11_3, tf11_4, tf11_5, tf11_6, tf11_7, tf11_8, tf11_9, tf11_10, tf11_11])
        db.commit()

        # T12 – UML
        tf12_1 = TecnicaFacetaValor(tecnica_id=tecnica_t12.id, faceta_valor_id=valor_faceta_f1_2.id)  # F1 (Semi-formal)
        tf12_2 = TecnicaFacetaValor(tecnica_id=tecnica_t12.id, faceta_valor_id=valor_faceta_f2_2.id)  # F2 (Média)
        tf12_3 = TecnicaFacetaValor(tecnica_id=tecnica_t12.id, faceta_valor_id=valor_faceta_f3_3.id)  # F3 (Presente)
        tf12_4 = TecnicaFacetaValor(tecnica_id=tecnica_t12.id, faceta_valor_id=valor_faceta_f4_2.id)  # F4 (Parcial)
        tf12_5 = TecnicaFacetaValor(tecnica_id=tecnica_t12.id, faceta_valor_id=valor_faceta_f5_2.id)  # F5 (Média)
        tf12_6 = TecnicaFacetaValor(tecnica_id=tecnica_t12.id, faceta_valor_id=valor_faceta_f6_3.id)  # F6 (Alta)
        tf12_7 = TecnicaFacetaValor(tecnica_id=tecnica_t12.id, faceta_valor_id=valor_faceta_f7_1.id)  # F7 (Nenhum)
        tf12_8 = TecnicaFacetaValor(tecnica_id=tecnica_t12.id, faceta_valor_id=valor_faceta_f8_2.id)  # F8 (Negócios)
        tf12_9 = TecnicaFacetaValor(tecnica_id=tecnica_t12.id, faceta_valor_id=valor_faceta_f9_2.id)  # F9 (Gráfica)
        tf12_10 = TecnicaFacetaValor(tecnica_id=tecnica_t12.id, faceta_valor_id=valor_faceta_f10_2.id)  # F10 (Média)
        tf12_11 = TecnicaFacetaValor(tecnica_id=tecnica_t12.id, faceta_valor_id=valor_faceta_f11_2.id)  # F11 (Média)
        db.add_all([tf12_1, tf12_2, tf12_3, tf12_4, tf12_5, tf12_6, tf12_7, tf12_8, tf12_9, tf12_10, tf12_11])
        db.commit()

        # T13 – BPMN
        tf13_1 = TecnicaFacetaValor(tecnica_id=tecnica_t13.id, faceta_valor_id=valor_faceta_f1_2.id)  # F1 (Semi-formal)
        tf13_2 = TecnicaFacetaValor(tecnica_id=tecnica_t13.id, faceta_valor_id=valor_faceta_f2_2.id)  # F2 (Média)
        tf13_3 = TecnicaFacetaValor(tecnica_id=tecnica_t13.id, faceta_valor_id=valor_faceta_f3_2.id)  # F3 (Parcial)
        tf13_4 = TecnicaFacetaValor(tecnica_id=tecnica_t13.id, faceta_valor_id=valor_faceta_f4_1.id)  # F4 (Inexistente)
        tf13_5 = TecnicaFacetaValor(tecnica_id=tecnica_t13.id, faceta_valor_id=valor_faceta_f5_2.id)  # F5 (Média)
        tf13_6 = TecnicaFacetaValor(tecnica_id=tecnica_t13.id, faceta_valor_id=valor_faceta_f6_2.id)  # F6 (Média)
        tf13_7 = TecnicaFacetaValor(tecnica_id=tecnica_t13.id, faceta_valor_id=valor_faceta_f7_1.id)  # F7 (Nenhum)
        tf13_8 = TecnicaFacetaValor(tecnica_id=tecnica_t13.id, faceta_valor_id=valor_faceta_f8_2.id)  # F8 (Negócios)
        tf13_9 = TecnicaFacetaValor(tecnica_id=tecnica_t13.id, faceta_valor_id=valor_faceta_f9_2.id)  # F9 (Gráfica)
        tf13_10 = TecnicaFacetaValor(tecnica_id=tecnica_t13.id, faceta_valor_id=valor_faceta_f10_2.id)  # F10 (Média)
        tf13_11 = TecnicaFacetaValor(tecnica_id=tecnica_t13.id, faceta_valor_id=valor_faceta_f11_2.id)  # F11 (Média)
        db.add_all([tf13_1, tf13_2, tf13_3, tf13_4, tf13_5, tf13_6, tf13_7, tf13_8, tf13_9, tf13_10, tf13_11])
        db.commit()

        # T14 – EPC
        tf14_1 = TecnicaFacetaValor(tecnica_id=tecnica_t14.id, faceta_valor_id=valor_faceta_f1_2.id)  # F1 (Semi-formal)
        tf14_2 = TecnicaFacetaValor(tecnica_id=tecnica_t14.id, faceta_valor_id=valor_faceta_f2_1.id)  # F2 (Alta)
        tf14_3 = TecnicaFacetaValor(tecnica_id=tecnica_t14.id, faceta_valor_id=valor_faceta_f3_2.id)  # F3 (Parcial)
        tf14_4 = TecnicaFacetaValor(tecnica_id=tecnica_t14.id, faceta_valor_id=valor_faceta_f4_1.id)  # F4 (Inexistente)
        tf14_5 = TecnicaFacetaValor(tecnica_id=tecnica_t14.id, faceta_valor_id=valor_faceta_f5_2.id)  # F5 (Média)
        tf14_6 = TecnicaFacetaValor(tecnica_id=tecnica_t14.id, faceta_valor_id=valor_faceta_f6_2.id)  # F6 (Média)
        tf14_7 = TecnicaFacetaValor(tecnica_id=tecnica_t14.id, faceta_valor_id=valor_faceta_f7_1.id)  # F7 (Nenhum)
        tf14_8 = TecnicaFacetaValor(tecnica_id=tecnica_t14.id, faceta_valor_id=valor_faceta_f8_2.id)  # F8 (Negócios)
        tf14_9 = TecnicaFacetaValor(tecnica_id=tecnica_t14.id, faceta_valor_id=valor_faceta_f9_2.id)  # F9 (Gráfica)
        tf14_10 = TecnicaFacetaValor(tecnica_id=tecnica_t14.id, faceta_valor_id=valor_faceta_f10_2.id)  # F10 (Média)
        tf14_11 = TecnicaFacetaValor(tecnica_id=tecnica_t14.id, faceta_valor_id=valor_faceta_f11_1.id)  # F11 (Baixa)
        db.add_all([tf14_1, tf14_2, tf14_3, tf14_4, tf14_5, tf14_6, tf14_7, tf14_8, tf14_9, tf14_10, tf14_11])
        db.commit()

        # T15 – User Stories
        tf15_1 = TecnicaFacetaValor(tecnica_id=tecnica_t15.id, faceta_valor_id=valor_faceta_f1_3.id)  # F1 (Informal)
        tf15_2 = TecnicaFacetaValor(tecnica_id=tecnica_t15.id, faceta_valor_id=valor_faceta_f2_1.id)  # F2 (Alta)
        tf15_3 = TecnicaFacetaValor(tecnica_id=tecnica_t15.id, faceta_valor_id=valor_faceta_f3_2.id)  # F3 (Parcial)
        tf15_4 = TecnicaFacetaValor(tecnica_id=tecnica_t15.id, faceta_valor_id=valor_faceta_f4_1.id)  # F4 (Inexistente)
        tf15_5 = TecnicaFacetaValor(tecnica_id=tecnica_t15.id, faceta_valor_id=valor_faceta_f5_2.id)  # F5 (Média)
        tf15_6 = TecnicaFacetaValor(tecnica_id=tecnica_t15.id, faceta_valor_id=valor_faceta_f6_2.id)  # F6 (Média)
        tf15_7 = TecnicaFacetaValor(tecnica_id=tecnica_t15.id, faceta_valor_id=valor_faceta_f7_1.id)  # F7 (Nenhum)
        tf15_8 = TecnicaFacetaValor(tecnica_id=tecnica_t15.id, faceta_valor_id=valor_faceta_f8_1.id)  # F8 (Geral)
        tf15_9 = TecnicaFacetaValor(tecnica_id=tecnica_t15.id, faceta_valor_id=valor_faceta_f9_1.id)  # F9 (Textual)
        tf15_10 = TecnicaFacetaValor(tecnica_id=tecnica_t15.id, faceta_valor_id=valor_faceta_f10_1.id)  # F10 (Alta)
        tf15_11 = TecnicaFacetaValor(tecnica_id=tecnica_t15.id, faceta_valor_id=valor_faceta_f11_1.id)  # F11 (Baixa)
        db.add_all([tf15_1, tf15_2, tf15_3, tf15_4, tf15_5, tf15_6, tf15_7, tf15_8, tf15_9, tf15_10, tf15_11])
        db.commit()

        # 5. QUESTÕES
        questao1 = Questao(codigo="Q1", conteudo="Que tipo de sistema você está especificando?")
        questao2 = Questao(codigo="Q2",
                           conteudo="Você precisa evitar interpretações diferentes dos requisitos (ambiguidade)?")
        questao3 = Questao(codigo="Q3",
                           conteudo="Os usuários ou clientes que vão validar os requisitos têm perfil técnico?")
        questao4 = Questao(codigo="Q4", conteudo="O projeto vai usar práticas ágeis (como Scrum, Kanban, XP)?")
        questao5 = Questao(codigo="Q5",
                           conteudo="O sistema precisa reagir a eventos externos ou tempo real (por exemplo, sensores, chamadas, mensagens)?")
        questao6 = Questao(codigo="Q6",
                           conteudo="Você pretende usar ferramentas que gerem automaticamente diagramas, protótipos ou testes?")
        questao7 = Questao(codigo="Q7",
                           conteudo="Sua equipe tem familiaridade com métodos formais ou prefere técnicas mais simples e visuais?")
        questao8 = Questao(codigo="Q8",
                           conteudo="Você prefere trabalhar com texto ou diagramas visuais para representar requisitos?")
        questao9 = Questao(codigo="Q9",
                           conteudo="Você quer que a especificação sirva de base direta para desenvolvimento e testes?")
        questao10 = Questao(codigo="Q10",
                            conteudo="Quão importante é garantir automaticamente que os requisitos estejam consistentes ou sem erros?")
        questao11 = Questao(codigo="Q11",
                            conteudo="Você quer que a técnica ajude a organizar os requisitos (por exemplo, em níveis ou seções bem definidos)?")

        db.add_all([
            questao1, questao2, questao3, questao4, questao5,
            questao6, questao7, questao8, questao9, questao10, questao11
        ])
        db.commit()

        # 6. RESPOSTAS

        # QUESTÃO 1
        resposta_q1_1 = Resposta(questao_id=questao1.id, conteudo="Sistema de negócio / gestão")
        resposta_q1_2 = Resposta(questao_id=questao1.id, conteudo="Sistema embarcado / tempo real")
        resposta_q1_3 = Resposta(questao_id=questao1.id, conteudo="Outro / genérico")
        db.add_all([resposta_q1_1, resposta_q1_2, resposta_q1_3])
        db.commit()

        # QUESTÃO 2
        resposta_q2_1 = Resposta(questao_id=questao2.id, conteudo="Sim, totalmente")
        resposta_q2_2 = Resposta(questao_id=questao2.id, conteudo="Parcialmente")
        resposta_q2_3 = Resposta(questao_id=questao2.id, conteudo="Não, o suficiente é entender a ideia geral")
        db.add_all([resposta_q2_1, resposta_q2_2, resposta_q2_3])
        db.commit()

        # QUESTÃO 3
        resposta_q3_1 = Resposta(questao_id=questao3.id, conteudo="Sim, técnicos")
        resposta_q3_2 = Resposta(questao_id=questao3.id, conteudo="Misto")
        resposta_q3_3 = Resposta(questao_id=questao3.id, conteudo="Não, são de negócio")
        db.add_all([resposta_q3_1, resposta_q3_2, resposta_q3_3])
        db.commit()

        # QUESTÃO 4
        resposta_q4_1 = Resposta(questao_id=questao4.id, conteudo="Sim")
        resposta_q4_2 = Resposta(questao_id=questao4.id, conteudo="Não")
        db.add_all([resposta_q4_1, resposta_q4_2])
        db.commit()

        # QUESTÃO 5
        resposta_q5_1 = Resposta(questao_id=questao5.id, conteudo="Sim, bastante")
        resposta_q5_2 = Resposta(questao_id=questao5.id, conteudo="Parcialmente")
        resposta_q5_3 = Resposta(questao_id=questao5.id, conteudo="Não")
        db.add_all([resposta_q5_1, resposta_q5_2, resposta_q5_3])
        db.commit()

        # QUESTÃO 6
        resposta_q6_1 = Resposta(questao_id=questao6.id, conteudo="Sim, testes")
        resposta_q6_2 = Resposta(questao_id=questao6.id, conteudo="Sim, protótipos")
        resposta_q6_3 = Resposta(questao_id=questao6.id, conteudo="Não")
        db.add_all([resposta_q6_1, resposta_q6_2, resposta_q6_3])
        db.commit()

        # QUESTÃO 7
        resposta_q7_1 = Resposta(questao_id=questao7.id, conteudo="Alta experiência técnica")
        resposta_q7_2 = Resposta(questao_id=questao7.id, conteudo="Alguma")
        resposta_q7_3 = Resposta(questao_id=questao7.id, conteudo="Prefere simplicidade")
        db.add_all([resposta_q7_1, resposta_q7_2, resposta_q7_3])
        db.commit()

        # QUESTÃO 8
        resposta_q8_1 = Resposta(questao_id=questao8.id, conteudo="Texto")
        resposta_q8_2 = Resposta(questao_id=questao8.id, conteudo="Diagramas")
        resposta_q8_3 = Resposta(questao_id=questao8.id, conteudo="Tanto Faz")
        db.add_all([resposta_q8_1, resposta_q8_2, resposta_q8_3])
        db.commit()

        # QUESTÃO 9
        resposta_q9_1 = Resposta(questao_id=questao9.id, conteudo="Sim")
        resposta_q9_2 = Resposta(questao_id=questao9.id, conteudo="Em parte")
        resposta_q9_3 = Resposta(questao_id=questao9.id, conteudo="Não necessariamente")
        db.add_all([resposta_q9_1, resposta_q9_2, resposta_q9_3])
        db.commit()

        # QUESTÃO 10
        resposta_q10_1 = Resposta(questao_id=questao10.id, conteudo="Muito importante")
        resposta_q10_2 = Resposta(questao_id=questao10.id, conteudo="Moderadamente")
        resposta_q10_3 = Resposta(questao_id=questao10.id, conteudo="Pouco importante")
        db.add_all([resposta_q10_1, resposta_q10_2, resposta_q10_3])
        db.commit()

        # QUESTÃO 11
        resposta_q11_1 = Resposta(questao_id=questao11.id, conteudo="Sim")
        resposta_q11_2 = Resposta(questao_id=questao11.id, conteudo="Em parte")
        resposta_q11_3 = Resposta(questao_id=questao11.id, conteudo="Não é prioridade")
        db.add_all([resposta_q11_1, resposta_q11_2, resposta_q11_3])
        db.commit()

        # 7. ASSOCIAÇÃO RESPOSTA-FACETA (Onde o seu algoritmo de interpretação entra)

        # Q1 x F8

        rfv1 = RespostaFacetaValor(
            resposta_id=resposta_q1_1.id,
            faceta_valor_id=valor_faceta_f8_1.id,
            pontuacao=0.5
        )
        rfv2 = RespostaFacetaValor(
            resposta_id=resposta_q1_2.id,
            faceta_valor_id=valor_faceta_f8_1.id,
            pontuacao=0.5
        )
        rfv3 = RespostaFacetaValor(
            resposta_id=resposta_q1_3.id,
            faceta_valor_id=valor_faceta_f8_1.id,
            pontuacao=1
        )

        rfv4 = RespostaFacetaValor(
            resposta_id=resposta_q1_1.id,
            faceta_valor_id=valor_faceta_f8_2.id,
            pontuacao=1
        )
        rfv5 = RespostaFacetaValor(
            resposta_id=resposta_q1_2.id,
            faceta_valor_id=valor_faceta_f8_2.id,
            pontuacao=0
        )
        rfv6 = RespostaFacetaValor(
            resposta_id=resposta_q1_3.id,
            faceta_valor_id=valor_faceta_f8_2.id,
            pontuacao=0
        )

        rfv7 = RespostaFacetaValor(
            resposta_id=resposta_q1_1.id,
            faceta_valor_id=valor_faceta_f8_3.id,
            pontuacao=0
        )
        rfv8 = RespostaFacetaValor(
            resposta_id=resposta_q1_2.id,
            faceta_valor_id=valor_faceta_f8_3.id,
            pontuacao=1
        )
        rfv9 = RespostaFacetaValor(
            resposta_id=resposta_q1_3.id,
            faceta_valor_id=valor_faceta_f8_3.id,
            pontuacao=0
        )
        db.add_all([rfv1, rfv2, rfv3, rfv4, rfv5, rfv6, rfv7, rfv8, rfv9])
        db.commit()

        # Q2 x F1

        rfv10 = RespostaFacetaValor(
            resposta_id=resposta_q2_1.id,
            faceta_valor_id=valor_faceta_f1_1.id,
            pontuacao=1
        )
        rfv11 = RespostaFacetaValor(
            resposta_id=resposta_q2_2.id,
            faceta_valor_id=valor_faceta_f1_1.id,
            pontuacao=0.5
        )
        rfv12 = RespostaFacetaValor(
            resposta_id=resposta_q2_3.id,
            faceta_valor_id=valor_faceta_f1_1.id,
            pontuacao=0
        )

        rfv13 = RespostaFacetaValor(
            resposta_id=resposta_q2_1.id,
            faceta_valor_id=valor_faceta_f1_2.id,
            pontuacao=0.5
        )
        rfv14 = RespostaFacetaValor(
            resposta_id=resposta_q2_2.id,
            faceta_valor_id=valor_faceta_f1_2.id,
            pontuacao=1
        )
        rfv15 = RespostaFacetaValor(
            resposta_id=resposta_q2_3.id,
            faceta_valor_id=valor_faceta_f1_2.id,
            pontuacao=0.5
        )

        rfv16 = RespostaFacetaValor(
            resposta_id=resposta_q2_1.id,
            faceta_valor_id=valor_faceta_f1_3.id,
            pontuacao=0
        )
        rfv17 = RespostaFacetaValor(
            resposta_id=resposta_q2_2.id,
            faceta_valor_id=valor_faceta_f1_3.id,
            pontuacao=0
        )
        rfv18 = RespostaFacetaValor(
            resposta_id=resposta_q2_3.id,
            faceta_valor_id=valor_faceta_f1_3.id,
            pontuacao=1
        )
        db.add_all([rfv10, rfv11, rfv12, rfv13, rfv14, rfv15, rfv16, rfv17, rfv18])
        db.commit()

        # Q3 x F2

        rfv19 = RespostaFacetaValor(
            resposta_id=resposta_q3_1.id,
            faceta_valor_id=valor_faceta_f2_1.id,
            pontuacao=0
        )
        rfv20 = RespostaFacetaValor(
            resposta_id=resposta_q3_2.id,
            faceta_valor_id=valor_faceta_f2_1.id,
            pontuacao=0.5
        )
        rfv21 = RespostaFacetaValor(
            resposta_id=resposta_q3_3.id,
            faceta_valor_id=valor_faceta_f2_1.id,
            pontuacao=1
        )

        rfv22 = RespostaFacetaValor(
            resposta_id=resposta_q3_1.id,
            faceta_valor_id=valor_faceta_f2_2.id,
            pontuacao=0.5
        )
        rfv23 = RespostaFacetaValor(
            resposta_id=resposta_q3_2.id,
            faceta_valor_id=valor_faceta_f2_2.id,
            pontuacao=1
        )
        rfv24 = RespostaFacetaValor(
            resposta_id=resposta_q3_3.id,
            faceta_valor_id=valor_faceta_f2_2.id,
            pontuacao=0.5
        )

        rfv25 = RespostaFacetaValor(
            resposta_id=resposta_q3_1.id,
            faceta_valor_id=valor_faceta_f2_3.id,
            pontuacao=1
        )
        rfv26 = RespostaFacetaValor(
            resposta_id=resposta_q3_2.id,
            faceta_valor_id=valor_faceta_f2_3.id,
            pontuacao=0
        )
        rfv27 = RespostaFacetaValor(
            resposta_id=resposta_q3_3.id,
            faceta_valor_id=valor_faceta_f2_3.id,
            pontuacao=0
        )
        db.add_all([rfv19, rfv20, rfv21, rfv22, rfv23, rfv24, rfv25, rfv26, rfv27])
        db.commit()

        # Q4 x F10

        rfv28 = RespostaFacetaValor(
            resposta_id=resposta_q4_1.id,
            faceta_valor_id=valor_faceta_f10_1.id,
            pontuacao=1
        )
        rfv29 = RespostaFacetaValor(
            resposta_id=resposta_q4_2.id,
            faceta_valor_id=valor_faceta_f10_1.id,
            pontuacao=0
        )

        rfv30 = RespostaFacetaValor(
            resposta_id=resposta_q4_1.id,
            faceta_valor_id=valor_faceta_f10_2.id,
            pontuacao=0.5
        )
        rfv31 = RespostaFacetaValor(
            resposta_id=resposta_q4_2.id,
            faceta_valor_id=valor_faceta_f10_2.id,
            pontuacao=0.5
        )

        rfv32 = RespostaFacetaValor(
            resposta_id=resposta_q4_1.id,
            faceta_valor_id=valor_faceta_f10_3.id,
            pontuacao=0
        )
        rfv33 = RespostaFacetaValor(
            resposta_id=resposta_q4_2.id,
            faceta_valor_id=valor_faceta_f10_3.id,
            pontuacao=1
        )
        db.add_all([rfv28, rfv29, rfv30, rfv31, rfv32, rfv33])
        db.commit()

        # Q5 x F5

        rfv34 = RespostaFacetaValor(
            resposta_id=resposta_q5_1.id,
            faceta_valor_id=valor_faceta_f5_1.id,
            pontuacao=0
        )
        rfv35 = RespostaFacetaValor(
            resposta_id=resposta_q5_2.id,
            faceta_valor_id=valor_faceta_f5_1.id,
            pontuacao=0
        )
        rfv36 = RespostaFacetaValor(
            resposta_id=resposta_q5_3.id,
            faceta_valor_id=valor_faceta_f5_1.id,
            pontuacao=1
        )

        rfv37 = RespostaFacetaValor(
            resposta_id=resposta_q5_1.id,
            faceta_valor_id=valor_faceta_f5_2.id,
            pontuacao=0.5
        )
        rfv38 = RespostaFacetaValor(
            resposta_id=resposta_q5_2.id,
            faceta_valor_id=valor_faceta_f5_2.id,
            pontuacao=1
        )
        rfv39 = RespostaFacetaValor(
            resposta_id=resposta_q5_3.id,
            faceta_valor_id=valor_faceta_f5_2.id,
            pontuacao=0.5
        )

        rfv40 = RespostaFacetaValor(
            resposta_id=resposta_q5_1.id,
            faceta_valor_id=valor_faceta_f5_3.id,
            pontuacao=1
        )
        rfv41 = RespostaFacetaValor(
            resposta_id=resposta_q5_2.id,
            faceta_valor_id=valor_faceta_f5_3.id,
            pontuacao=0.5
        )
        rfv42 = RespostaFacetaValor(
            resposta_id=resposta_q5_3.id,
            faceta_valor_id=valor_faceta_f5_3.id,
            pontuacao=0
        )
        db.add_all([rfv34, rfv35, rfv36, rfv37, rfv38, rfv39, rfv40, rfv41, rfv42])
        db.commit()

        # Q6 x F7

        rfv43 = RespostaFacetaValor(
            resposta_id=resposta_q6_1.id,
            faceta_valor_id=valor_faceta_f7_1.id,
            pontuacao=0
        )
        rfv44 = RespostaFacetaValor(
            resposta_id=resposta_q6_2.id,
            faceta_valor_id=valor_faceta_f7_1.id,
            pontuacao=0
        )
        rfv45 = RespostaFacetaValor(
            resposta_id=resposta_q6_3.id,
            faceta_valor_id=valor_faceta_f7_1.id,
            pontuacao=1
        )

        rfv46 = RespostaFacetaValor(
            resposta_id=resposta_q6_1.id,
            faceta_valor_id=valor_faceta_f7_2.id,
            pontuacao=0
        )
        rfv47 = RespostaFacetaValor(
            resposta_id=resposta_q6_2.id,
            faceta_valor_id=valor_faceta_f7_2.id,
            pontuacao=1
        )
        rfv48 = RespostaFacetaValor(
            resposta_id=resposta_q6_3.id,
            faceta_valor_id=valor_faceta_f7_2.id,
            pontuacao=0
        )

        rfv49 = RespostaFacetaValor(
            resposta_id=resposta_q6_1.id,
            faceta_valor_id=valor_faceta_f7_3.id,
            pontuacao=1
        )
        rfv50 = RespostaFacetaValor(
            resposta_id=resposta_q6_2.id,
            faceta_valor_id=valor_faceta_f7_3.id,
            pontuacao=0
        )
        rfv51 = RespostaFacetaValor(
            resposta_id=resposta_q6_3.id,
            faceta_valor_id=valor_faceta_f7_3.id,
            pontuacao=0
        )
        db.add_all([rfv43, rfv44, rfv45, rfv46, rfv47, rfv48, rfv49, rfv50, rfv51])
        db.commit()

        # Q7 x F11

        rfv52 = RespostaFacetaValor(
            resposta_id=resposta_q7_1.id,
            faceta_valor_id=valor_faceta_f11_1.id,
            pontuacao=0
        )
        rfv53 = RespostaFacetaValor(
            resposta_id=resposta_q7_2.id,
            faceta_valor_id=valor_faceta_f11_1.id,
            pontuacao=0.5
        )
        rfv54 = RespostaFacetaValor(
            resposta_id=resposta_q7_3.id,
            faceta_valor_id=valor_faceta_f11_1.id,
            pontuacao=1
        )

        rfv55 = RespostaFacetaValor(
            resposta_id=resposta_q7_1.id,
            faceta_valor_id=valor_faceta_f11_2.id,
            pontuacao=0.5
        )
        rfv56 = RespostaFacetaValor(
            resposta_id=resposta_q7_2.id,
            faceta_valor_id=valor_faceta_f11_2.id,
            pontuacao=1
        )
        rfv57 = RespostaFacetaValor(
            resposta_id=resposta_q7_3.id,
            faceta_valor_id=valor_faceta_f11_2.id,
            pontuacao=0.5
        )

        rfv58 = RespostaFacetaValor(
            resposta_id=resposta_q7_1.id,
            faceta_valor_id=valor_faceta_f11_3.id,
            pontuacao=1
        )
        rfv59 = RespostaFacetaValor(
            resposta_id=resposta_q7_2.id,
            faceta_valor_id=valor_faceta_f11_3.id,
            pontuacao=0
        )
        rfv60 = RespostaFacetaValor(
            resposta_id=resposta_q7_3.id,
            faceta_valor_id=valor_faceta_f11_3.id,
            pontuacao=0
        )
        db.add_all([rfv52, rfv53, rfv54, rfv55, rfv56, rfv57, rfv58, rfv59, rfv60])
        db.commit()

        # Q8 x F9

        rfv61 = RespostaFacetaValor(
            resposta_id=resposta_q8_1.id,
            faceta_valor_id=valor_faceta_f9_1.id,
            pontuacao=1
        )
        rfv62 = RespostaFacetaValor(
            resposta_id=resposta_q8_2.id,
            faceta_valor_id=valor_faceta_f9_1.id,
            pontuacao=0
        )
        rfv63 = RespostaFacetaValor(
            resposta_id=resposta_q8_3.id,
            faceta_valor_id=valor_faceta_f9_1.id,
            pontuacao=0.5
        )

        rfv64 = RespostaFacetaValor(
            resposta_id=resposta_q8_1.id,
            faceta_valor_id=valor_faceta_f9_2.id,
            pontuacao=0
        )
        rfv65 = RespostaFacetaValor(
            resposta_id=resposta_q8_2.id,
            faceta_valor_id=valor_faceta_f9_2.id,
            pontuacao=1
        )
        rfv66 = RespostaFacetaValor(
            resposta_id=resposta_q8_3.id,
            faceta_valor_id=valor_faceta_f9_2.id,
            pontuacao=0.5
        )
        db.add_all([rfv61, rfv62, rfv63, rfv64, rfv65, rfv66])
        db.commit()

        # Q9 x F3

        rfv67 = RespostaFacetaValor(
            resposta_id=resposta_q9_1.id,
            faceta_valor_id=valor_faceta_f3_1.id,
            pontuacao=0
        )
        rfv68 = RespostaFacetaValor(
            resposta_id=resposta_q9_2.id,
            faceta_valor_id=valor_faceta_f3_1.id,
            pontuacao=0
        )
        rfv69 = RespostaFacetaValor(
            resposta_id=resposta_q9_3.id,
            faceta_valor_id=valor_faceta_f3_1.id,
            pontuacao=1
        )

        rfv70 = RespostaFacetaValor(
            resposta_id=resposta_q9_1.id,
            faceta_valor_id=valor_faceta_f3_2.id,
            pontuacao=0.5
        )
        rfv71 = RespostaFacetaValor(
            resposta_id=resposta_q9_2.id,
            faceta_valor_id=valor_faceta_f3_2.id,
            pontuacao=1
        )
        rfv72 = RespostaFacetaValor(
            resposta_id=resposta_q9_3.id,
            faceta_valor_id=valor_faceta_f3_2.id,
            pontuacao=0.5
        )

        rfv73 = RespostaFacetaValor(
            resposta_id=resposta_q9_1.id,
            faceta_valor_id=valor_faceta_f3_3.id,
            pontuacao=1
        )
        rfv74 = RespostaFacetaValor(
            resposta_id=resposta_q9_2.id,
            faceta_valor_id=valor_faceta_f3_3.id,
            pontuacao=0.5
        )
        rfv75 = RespostaFacetaValor(
            resposta_id=resposta_q9_3.id,
            faceta_valor_id=valor_faceta_f3_3.id,
            pontuacao=0
        )
        db.add_all([rfv67, rfv68, rfv69, rfv70, rfv71, rfv72, rfv73, rfv74, rfv75])
        db.commit()

        # Q10 x F4

        rfv76 = RespostaFacetaValor(
            resposta_id=resposta_q10_1.id,
            faceta_valor_id=valor_faceta_f4_1.id,
            pontuacao=0
        )
        rfv77 = RespostaFacetaValor(
            resposta_id=resposta_q10_2.id,
            faceta_valor_id=valor_faceta_f4_1.id,
            pontuacao=0
        )
        rfv78 = RespostaFacetaValor(
            resposta_id=resposta_q10_3.id,
            faceta_valor_id=valor_faceta_f4_1.id,
            pontuacao=1
        )

        rfv79 = RespostaFacetaValor(
            resposta_id=resposta_q10_1.id,
            faceta_valor_id=valor_faceta_f4_2.id,
            pontuacao=0.5
        )
        rfv80 = RespostaFacetaValor(
            resposta_id=resposta_q10_2.id,
            faceta_valor_id=valor_faceta_f4_2.id,
            pontuacao=1
        )
        rfv81 = RespostaFacetaValor(
            resposta_id=resposta_q10_3.id,
            faceta_valor_id=valor_faceta_f4_2.id,
            pontuacao=0.5
        )

        rfv82 = RespostaFacetaValor(
            resposta_id=resposta_q10_1.id,
            faceta_valor_id=valor_faceta_f4_3.id,
            pontuacao=1
        )
        rfv83 = RespostaFacetaValor(
            resposta_id=resposta_q10_2.id,
            faceta_valor_id=valor_faceta_f4_3.id,
            pontuacao=0.5
        )
        rfv84 = RespostaFacetaValor(
            resposta_id=resposta_q10_3.id,
            faceta_valor_id=valor_faceta_f4_3.id,
            pontuacao=0
        )
        db.add_all([rfv76, rfv77, rfv78, rfv79, rfv80, rfv81, rfv82, rfv83, rfv84])
        db.commit()

        # Q11 x F6

        rfv85 = RespostaFacetaValor(
            resposta_id=resposta_q11_1.id,
            faceta_valor_id=valor_faceta_f6_1.id,
            pontuacao=0
        )
        rfv86 = RespostaFacetaValor(
            resposta_id=resposta_q11_2.id,
            faceta_valor_id=valor_faceta_f6_1.id,
            pontuacao=0
        )
        rfv87 = RespostaFacetaValor(
            resposta_id=resposta_q11_3.id,
            faceta_valor_id=valor_faceta_f6_1.id,
            pontuacao=1
        )

        rfv88 = RespostaFacetaValor(
            resposta_id=resposta_q11_1.id,
            faceta_valor_id=valor_faceta_f6_2.id,
            pontuacao=0.5
        )
        rfv89 = RespostaFacetaValor(
            resposta_id=resposta_q11_2.id,
            faceta_valor_id=valor_faceta_f6_2.id,
            pontuacao=1
        )
        rfv90 = RespostaFacetaValor(
            resposta_id=resposta_q11_3.id,
            faceta_valor_id=valor_faceta_f6_2.id,
            pontuacao=0.5
        )

        rfv91 = RespostaFacetaValor(
            resposta_id=resposta_q11_1.id,
            faceta_valor_id=valor_faceta_f6_3.id,
            pontuacao=1
        )
        rfv92 = RespostaFacetaValor(
            resposta_id=resposta_q11_2.id,
            faceta_valor_id=valor_faceta_f6_3.id,
            pontuacao=0.5
        )
        rfv93 = RespostaFacetaValor(
            resposta_id=resposta_q11_3.id,
            faceta_valor_id=valor_faceta_f6_3.id,
            pontuacao=0
        )
        db.add_all([rfv85, rfv86, rfv87, rfv88, rfv89, rfv90, rfv91, rfv92, rfv93])
        db.commit()

        print("--- DADOS INICIAIS INSERIDOS COM SUCESSO ---")

    except IntegrityError as e:
        db.rollback()
        print("AVISO: Dados iniciais já existem ou houve um erro de integridade. Rollback executado.")
        # print(e)
    except Exception as e:
        db.rollback()
        print(f"ERRO FATAL ao inserir dados: {e}")

    finally:
        db.close()


def initialize_database():
    print("A criar tabelas no PostgreSQL...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas/verificadas.")

    db = SessionLocal()
    create_initial_data(db)


if __name__ == "__main__":
    initialize_database()
