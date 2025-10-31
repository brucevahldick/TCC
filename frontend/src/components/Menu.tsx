import {Link, useLocation} from "react-router-dom";

export function Menu() {
    const location = useLocation();

    const tecnicasEspecificacao = "Técnicas de Especificação";
    const questionario = "Questionário";
    const guiaFacetado = "Guia Facetado";

    const isActive = (path: string) =>
        location.pathname === path ? "ativo" : "";

    return (
        <div className="menu-container">
            <h1>{questionario}</h1>
            <nav className="menu">
                <ul>
                    <li className={isActive("/tecnicas-especificacao")}>
                        <Link to="/tecnicas-especificacao">{tecnicasEspecificacao}</Link>
                    </li>
                    <li className={isActive("/")}>
                        <Link to="/">{questionario}</Link>
                    </li>
                    <li className={isActive("/guia-facetado")}>
                        <Link to="/guia-facetado">{guiaFacetado}</Link>
                    </li>
                </ul>
            </nav>
        </div>
    );
}
