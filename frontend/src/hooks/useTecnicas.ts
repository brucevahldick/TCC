import {useEffect, useState} from "react";
import {getTecnicasDetalhadas} from "../services/api";

let tecnicasCache = [];

export function useTecnicas() {
    const [tecnicas, setTecnicas] = useState([]);
    const [erro, setErro] = useState<string | null>(null);

    useEffect(() => {
        if (tecnicasCache.length > 0) {
            setTecnicas(tecnicasCache);
            return;
        }

        getTecnicasDetalhadas()
            .then((data) => {
                tecnicasCache = data.questoes || [];
                setTecnicas(tecnicasCache);
            })
            .catch((err) =>
                setErro(err instanceof Error ? err.message : "Erro desconhecido")
            );
    }, []);

    return {
        tecnicas: tecnicas,
        erro
    };
}