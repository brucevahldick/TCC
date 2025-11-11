import {useRecomendacoes} from "../hooks/useRecomendacoes.ts";
import {useQuestoes} from "../hooks/useQuestoes.ts";
import {Recomendacoes} from "./Recomendacoes.tsx";
import {useNavigate} from "react-router-dom";
import {useEffect} from "react";

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
        <Recomendacoes tecnicas={recomendacoes} onResponderNovamente={handleResponderNovamente}/>
    );
}
