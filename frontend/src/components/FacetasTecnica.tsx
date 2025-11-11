export function FacetasTecnica({facetas}) {
    return (
        <div className="facetas-list">
            {facetas.map((faceta, index) => (
                <div key={index} className="faceta-item">
                    <div className="faceta-title" title={faceta.definicao}>{faceta.nome}</div>
                    <span className="faceta-value">{faceta.valor_associado.valor}</span>
                </div>
            ))}
        </div>
    );
}