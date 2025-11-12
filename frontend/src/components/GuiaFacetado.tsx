import {useEffect, useState} from "react";
import {getGuiaFacetadoData} from "../services/api.ts";
import {Loading} from "./Loading.tsx";
import {TecnicaDetalhada} from "./TecnicasEspecificacao.tsx";
import {TabelaFacetas} from "./TabelaFacetas.tsx";
import {ListaFacetas} from "./ListaFacetas.tsx";

interface FacetaGuia {
    codigo: string;
    nome: string;
    definicao: string | null;
    valores_possiveis: string[];
}

interface GuiaFacetadoData {
    tecnicas: TecnicaDetalhada[];
    facetas: FacetaGuia[];
}

export function GuiaFacetado() {
    const [data, setData] = useState<GuiaFacetadoData | null>(null);
    const [loading, setLoading] = useState(true);
    const [erro, setErro] = useState<string | null>(null);

    useEffect(() => {
        getGuiaFacetadoData()
            .then((data) => {
                setData(data);
            })
            .catch((err) => {
                setErro(err instanceof Error ? err.message : "Erro desconhecido ao buscar dados do Guia Facetado");
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

    if (!data || data.tecnicas.length === 0 || data.facetas.length === 0) {
        return <p>Nenhum dado encontrado para o Guia Facetado.</p>;
    }

    return (
        <div className="guia-facetado">
            <TabelaFacetas tecnicas={data.tecnicas} facetas={data.facetas}/>
            <ListaFacetas facetas={data.facetas}/>
        </div>
    );
}
