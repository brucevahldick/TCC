import {useState, createContext, useContext} from "react";

export interface Tecnica {
    id: number;
    nome: string;
    codigo: string;
    pontuacao: number;
}

export const RecomendacoesContext = createContext(null);

export function useRecomendacoesProvider() {
    const [recomendacoes, setRecomendacoes] = useState<Tecnica[]>([]);

    const setRecomendacoesGlobais = (tecnicas: Tecnica[]) => {
        setRecomendacoes(tecnicas);
    };

    const limparRecomendacoes = () => {
        setRecomendacoes([]);
    };

    return {
        recomendacoes,
        setRecomendacoesGlobais,
        limparRecomendacoes,
    };
}

export function useRecomendacoes() {
    return useContext(RecomendacoesContext);
}
