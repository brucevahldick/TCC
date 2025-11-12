import {Recomendacao} from "./Recomendacao.tsx";

export function ListaRecomendacoes({tecnicas}) {
    return (
        <div className="tecnicas-listagem">
            {tecnicas.map((t) => (
                <Recomendacao tecnica={t}></Recomendacao>
            ))}
        </div>
    );
}
