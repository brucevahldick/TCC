import {FacetasTecnica} from "./FacetasTecnica.tsx";
import {InfoTecnica} from "./InfoTecnica.tsx";

export function Tecnica({tecnica}) {
    return (
        <section key={tecnica.id} id={tecnica.codigo.toLowerCase()} className="tecnica-section">
            <InfoTecnica tecnica={tecnica}/>
            <FacetasTecnica facetas={tecnica.facetas}/>
        </section>
    );
}