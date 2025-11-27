import {FacetaValor} from "./FacetaValor.tsx";

export function Faceta({faceta}: { faceta: any }) {
    return (
        <section id={faceta.codigo.toLowerCase()} key={faceta.codigo} className="faceta-section">
            <h3>{faceta.nome} ({faceta.codigo})</h3>
            <p> {faceta.definicao || "N/A"}</p>
            <div className="valores-faceta">
                {faceta.valores_possiveis.map((valor: any) => (
                    <FacetaValor valor={valor}></FacetaValor>
                ))}
            </div>
        </section>
    );
}