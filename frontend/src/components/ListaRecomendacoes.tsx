import {Recomendacao} from "./Recomendacao.tsx";

export function ListaRecomendacoes({tecnicas}: { tecnicas: any }) {
    return (
        <div className="tecnicas-listagem">
            {tecnicas.map((t: any) => (
                <Recomendacao tecnica={t}></Recomendacao>
            ))}
        </div>
    );
}
