import {Questao} from "./Questao.tsx";
import {useState} from "react";
import {useQuestoes} from "../hooks/useQuestoes.ts";
import {postRespostas} from "../services/api.ts";
import {Recomendacoes} from "./Recomendacoes.tsx";
import {Loading} from "./Loading.tsx";

export function Questionario() {
    const {questoes, erro} = useQuestoes();
    const [recomendacoes, setRecomendacoes] = useState([]);
    const [loading, setLoading] = useState(false);
    const [respostasSelecionadas, setRespostasSelecionadas] = useState({});

    const handleSelectResposta = (questaoId: number, respostaId: number) => {
        setRespostasSelecionadas((prev) => ({...prev, [questaoId]: respostaId}));
    };

    const handleSubmit = async () => {
        const respostas = Object.values(respostasSelecionadas);
        if (respostas.length === 0) {
            alert("Selecione ao menos uma resposta antes de enviar.");
            return;
        }

        setLoading(true);
        try {
            const data = await postRespostas(respostas);
            setRecomendacoes(data.tecnicas || []);
        } catch (err) {
            alert(err instanceof Error ? err.message : "Erro desconhecido");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            {recomendacoes.length > 0 ? (<Recomendacoes tecnicas={recomendacoes}/>) : (<div className="questionario">
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
            </div>)
            }
        </div>

    );
}