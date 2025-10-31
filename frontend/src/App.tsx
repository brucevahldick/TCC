import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import {Menu} from "./components/Menu";
import {Questionario} from "./components/Questionario";
import {TecnicasEspecificacao} from "./components/TecnicasEspecificacao.tsx";
import {GuiaFacetado} from "./components/GuiaFacetado.tsx";
import "./App.scss";

export default function App() {
    return (
        <Router>
            <div className="app-container">
                <Menu/>
                <div className="conteudo">
                    <Routes>
                        <Route path="/tecnicas-especificacao" element={<TecnicasEspecificacao/>}/>
                        <Route path="/" element={<Questionario/>}/>
                        <Route path="/guia-facetado" element={<GuiaFacetado/>}/>
                    </Routes>
                </div>
            </div>
        </Router>
    );
}
