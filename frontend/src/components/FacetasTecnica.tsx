import {Link} from "react-router-dom";
import {FacetaValor} from "./FacetaValor.tsx";

export function FacetasTecnica({facetas}) {
    return (
        <div className="facetas-list">
            {facetas.map((faceta, index) => (
                    <Link to={`/guia-facetado#${faceta.codigo.toLowerCase()}`}>
                        <div key={index} className="faceta-item">
                            <div className="faceta-title" title={faceta.definicao}>{faceta.nome}</div>
                            <FacetaValor valor={faceta.valor_associado.valor}></FacetaValor>
                        </div>
                    </Link>
                )
            )}
        </div>
    )
        ;
}