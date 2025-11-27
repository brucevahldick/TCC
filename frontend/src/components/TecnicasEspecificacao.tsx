import {useState, useEffect} from "react";
import {getTecnicasDetalhadas} from "../services/api";
import {Loading} from "./Loading";
import {Tecnica} from "./Tecnica.tsx";

interface FacetaValorDetalhe {
    valor: string | null;
    pontuacao: number | null;
}

interface FacetaDetalhe {
    codigo: string;
    nome: string;
    definicao: string | null;
    valor_associado: FacetaValorDetalhe;
}

export interface TecnicaDetalhada {
    id: number;
    codigo: string;
    nome: string;
    facetas: FacetaDetalhe[];
}

export function TecnicasEspecificacao() {
    const [tecnicas, setTecnicas] = useState<TecnicaDetalhada[]>([]);
    const [loading, setLoading] = useState(true);
    const [erro, setErro] = useState<string | null>(null);

    useEffect(() => {
        getTecnicasDetalhadas()
            .then((data) => {
                setTecnicas(data.tecnicas || []);
            })
            .catch((err) => {
                setErro(err instanceof Error ? err.message : "Erro desconhecido ao buscar técnicas");
            })
            .finally(() => {
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <Loading/>;
    }

    if (erro) {
        return <p className="erro">❌ {erro}</p>;
    }

    return (
        <div className="tecnicas-especificacao">
            {tecnicas.map((tecnica) => (
                <Tecnica tecnica={tecnica}></Tecnica>
            ))}
        </div>
    );
}
