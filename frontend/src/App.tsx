import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import ScrollToTop from "./components/ScrollToTop";
import {Menu} from "./components/Menu";
import {Questionario} from "./components/Questionario";
import {RecomendacoesPage} from "./components/RecomendacoesPage.tsx";
import {TecnicasEspecificacao} from "./components/TecnicasEspecificacao.tsx";
import {GuiaFacetado} from "./components/GuiaFacetado.tsx";
import {ScrollToTopButton} from "./components/ScrollToTopButton.tsx";
import {useRecomendacoesProvider, RecomendacoesContext} from "./hooks/useRecomendacoes.ts";
import "./App.scss";

function RecomendacoesProvider({children}) {
    const recomendacoesState = useRecomendacoesProvider();
    return (
        <RecomendacoesContext.Provider value={recomendacoesState}>
            {children}
        </RecomendacoesContext.Provider>
    );
}

export default function App() {
    return (
        <Router>
            <ScrollToTop/>
            <RecomendacoesProvider>
                <div className="app-container">
                    <Menu/>
                    <div className="conteudo">
                        <Routes>
                            <Route path="/" element={<Questionario/>}/>
                            <Route path="/tecnicas-especificacao" element={<TecnicasEspecificacao/>}/>
                            <Route path="/guia-facetado" element={<GuiaFacetado/>}/>
                            <Route path="/recomendacoes" element={<RecomendacoesPage/>}/>
                        </Routes>
                    </div>
                    <ScrollToTopButton/>
                </div>
            </RecomendacoesProvider>
        </Router>
    );
}
