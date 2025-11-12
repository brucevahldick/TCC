import React from "react";
import {Faceta} from "./Faceta.tsx";

interface FacetaGuia {
    codigo: string;
    nome: string;
    definicao: string | null;
    valores_possiveis: string[];
}

interface ListaFacetasProps {
    facetas: FacetaGuia[];
}

export function ListaFacetas({facetas}: ListaFacetasProps) {
    return (
        <div className="lista-facetas">
            {facetas.map(faceta => (
                <Faceta faceta={faceta}></Faceta>
            ))}
        </div>
    );
}
