export function InfoTecnica({tecnica}: { tecnica: any }) {
    return (
        <h2>{tecnica.nome} ({tecnica.codigo})</h2>
    );
}