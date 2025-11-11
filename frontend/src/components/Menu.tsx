import { Link, useLocation } from "react-router-dom";

export function Menu() {
    const location = useLocation();

    const rotas = [
        { path: "/", label: "Questionário" },
        { path: "/recomendacoes", label: "Recomendações" },
        { path: "/tecnicas-especificacao", label: "Técnicas de Especificação" },
        { path: "/guia-facetado", label: "Guia Facetado" },
    ];

    const tituloAtual =
        rotas.find((r) => r.path === location.pathname)?.label || "Questionário";

    const isActive = (path: string) =>
        location.pathname === path ? "ativo" : "";

    return (
        <div className="menu-container">
            <h1>{tituloAtual}</h1>
            <nav className="menu">
                <ul>
                    {rotas.map(({ path, label }) => (
                        <li key={path} className={isActive(path)}>
                            <Link to={path}>{label}</Link>
                        </li>
                    ))}
                </ul>
            </nav>
        </div>
    );
}
