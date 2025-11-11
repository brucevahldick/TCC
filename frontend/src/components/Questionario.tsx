import {Questao} from "./Questao.tsx";
import {useState} from "react";
import {useRecomendacoes} from "../hooks/useRecomendacoes.ts";
import {useNavigate} from "react-router-dom";
import {useQuestoes} from "../hooks/useQuestoes.ts";
import {postRespostas} from "../services/api.ts";

import {Loading} from "./Loading.tsx";

export function Questionario() {
    const {questoes, erro, respostasSelecionadas, handleSelectResposta} = useQuestoes();
    const {setRecomendacoesGlobais} = useRecomendacoes();
    const navigate = useNavigate();
    const [loading, setLoading] = useState(false);

    const handleSubmit = async () => {
        const respostas = Object.values(respostasSelecionadas).filter(r => r !== undefined);
        if (respostas.length === 0) {
            alert("Selecione ao menos uma resposta antes de enviar.");
            return;
        }

        setLoading(true);
        try {
            const data = await postRespostas(respostas);
            setRecomendacoesGlobais(data.tecnicas || []);
            navigate("/recomendacoes");
        } catch (err) {
            alert(err instanceof Error ? err.message : "Erro desconhecido");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="questionario">
            {erro && <p className="erro">❌ {erro}</p>}
            {!erro && questoes.length === 0 && <Loading/>}
            {questoes.map((q) => (
                <Questao
                    key={q.id}
                    questao={q}
                    respostaSelecionada={respostasSelecionadas[q.id]}
                    onSelect={handleSelectResposta}
                />
            ))}
            <div className="form-questionario">
                <button onClick={handleSubmit} disabled={loading || questoes.length === 0}>
                    {loading ? "Enviando..." : "Enviar"}
                </button>
            </div>
        </div>
    );
}