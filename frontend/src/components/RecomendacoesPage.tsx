import {useRecomendacoes} from "../hooks/useRecomendacoes.ts";
import {useQuestoes} from "../hooks/useQuestoes.ts";
import {ListaRecomendacoes} from "./ListaRecomendacoes.tsx";
import {useNavigate} from "react-router-dom";
import {useEffect} from "react";
import {GraficoRecomendacoes} from "./GraficoRecomendacoes.tsx";

export function RecomendacoesPage() {
    const {recomendacoes} = useRecomendacoes();
    const {limparRespostas} = useQuestoes();
    const navigate = useNavigate();

    useEffect(() => {
        if (recomendacoes.length === 0) {
            navigate("/");
        }
    }, [recomendacoes, navigate]);

    if (recomendacoes.length === 0) {
        return null;
    }

    const handleResponderNovamente = () => {
        limparRespostas();
        navigate("/");
    };

    return (
        <div className="recomendacoes">
            <GraficoRecomendacoes tecnicas={recomendacoes}></GraficoRecomendacoes>
            <div className="form-questionario">
                <button onClick={handleResponderNovamente}>
                    Responder Novamente
                </button>
            </div>
            <ListaRecomendacoes tecnicas={recomendacoes}/>
        </div>
    );
}
