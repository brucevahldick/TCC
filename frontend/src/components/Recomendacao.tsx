import {Link} from "react-router-dom";

export function Recomendacao({tecnica}) {
    return (
        <Link className="tecnica" to={`/tecnicas-especificacao#${tecnica.codigo.toLowerCase()}`}>
            <div>{tecnica.codigo}</div>
            <div className="nome-tecnica">{tecnica.nome}</div>
            <div>Pontuação: {(tecnica.pontuacao ?? 0).toFixed(2)}</div>
        </Link>
    );
}