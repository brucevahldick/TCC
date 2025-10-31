import {Link} from "react-router-dom";

export function Recomendacoes({ tecnicas }) {
    return (
        <div className="recomendacoes">
            <h2>Recomendações de Técnicas</h2>
            <ul>
                {tecnicas.map((t) => (
                    <li key={t.id}>
                        <strong>{t.nome}</strong> ({t.codigo}) — Pontuação:{" "}
                        {(t.pontuacao ?? 0).toFixed(2)}
                    </li>
                ))}
            </ul>
            <div className="form-questionario">
                <button>
                    <Link to="/">Responder Novamente</Link>
                </button>
            </div>
        </div>
    );
}
