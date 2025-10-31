import { useEffect, useState } from "react";
import { getQuestoes } from "../services/api";

export function useQuestoes() {
    const [questoes, setQuestoes] = useState([]);
    const [erro, setErro] = useState<string | null>(null);

    useEffect(() => {
        getQuestoes()
            .then((data) => setQuestoes(data.questoes || []))
            .catch((err) =>
                setErro(err instanceof Error ? err.message : "Erro desconhecido")
            );
    }, []);

    return { questoes, erro };
}
