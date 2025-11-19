import {useEffect, useState} from "react";
import {getQuestoes} from "../services/api";

let questoesCache: any[] = [];

export function useQuestoes() {
    const [questoes, setQuestoes] = useState<any[]>([]);
    const [erro, setErro] = useState<string | null>(null);

    // Estado para armazenar as respostas selecionadas
    const [respostasSelecionadas, setRespostasSelecionadas] = useState({});

    useEffect(() => {
        if (questoesCache.length > 0) {
            setQuestoes(questoesCache);
            return;
        }

        getQuestoes()
            .then((data) => {
                questoesCache = data.questoes || [];
                setQuestoes(questoesCache);
            })
            .catch((err) =>
                setErro(err instanceof Error ? err.message : "Erro desconhecido")
            );
    }, []);

    const handleSelectResposta = (questaoId: number, respostaId: number) => {
        setRespostasSelecionadas((prev) => ({...prev, [questaoId]: respostaId}));
    };

    const limparRespostas = () => {
        setRespostasSelecionadas({});
    };

    return {
        questoes,
        erro,
        respostasSelecionadas,
        handleSelectResposta,
        limparRespostas,
    };
}
