import React from "react";
import {Link} from "react-router-dom";
import {TecnicaDetalhada} from "./TecnicasEspecificacao.tsx";

interface FacetaGuia {
    codigo: string;
    nome: string;
    definicao: string | null;
    valores_possiveis: string[];
}

interface TabelaFacetasProps {
    tecnicas: TecnicaDetalhada[];
    facetas: FacetaGuia[];
}

export function TabelaFacetas({tecnicas, facetas}: TabelaFacetasProps) {
    // Extrair todos os códigos de facetas para o cabeçalho da tabela
    const facetaCodigos = facetas.map(f => f.codigo);

    // Mapear os valores das facetas para cada técnica
    const tecnicasMapeadas = tecnicas.map(tecnica => {
        const facetaValores: { [key: string]: string | null } = {};
        tecnica.facetas.forEach(faceta => {
            facetaValores[faceta.codigo] = faceta.valor_associado.valor;
        });
        return {
            codigo: tecnica.codigo,
            nome: tecnica.nome,
            facetaValores: facetaValores
        };
    });

    return (
        <div className="tabela-facetas">
            <table>
                <thead>
                <tr>
                    <th></th>
                    {facetas.map(faceta => (
                        <th title={faceta.nome} key={faceta.codigo}>
                            <Link to={`/guia-facetado#${faceta.codigo.toLowerCase()}`}>
                                {faceta.codigo}
                            </Link>
                        </th>
                    ))}
                </tr>
                </thead>
                <tbody>
                {tecnicasMapeadas.map(tecnica => (
                    <tr key={tecnica.codigo}>
                        <td title={tecnica.nome}>
                            <Link to={`/tecnicas-especificacao#${tecnica.codigo.toLowerCase()}`}>
                                {tecnica.codigo}
                            </Link>
                        </td>
                        {facetaCodigos.map(codigo => (
                            <td title={tecnica.facetaValores[codigo]} key={codigo}>
                                <Link title={tecnica.facetaValores[codigo]} to={`/guia-facetado#${codigo.toLowerCase()}`}>
                                    {tecnica.facetaValores[codigo] || "N/A"}
                                </Link>
                            </td>
                        ))}
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}
