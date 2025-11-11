import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    ResponsiveContainer,
} from "recharts";
import {Recomendacao} from "./Recomendacao.tsx";

export function Recomendacoes({tecnicas, onResponderNovamente}) {
    return (
        <div className="recomendacoes">
            <div style={{width: "100%", height: 300}}>
                <ResponsiveContainer width="100%" height="100%">
                    <BarChart
                        data={tecnicas.map((t) => ({
                            name: t.codigo,
                            Pontuação: parseFloat((t.pontuacao ?? 0).toFixed(2)),
                        }))}
                        margin={{
                            top: 5,
                            right: 30,
                            left: 20,
                            bottom: 5,
                        }}
                    >
                        <CartesianGrid strokeDasharray="3 3"/>
                        <XAxis dataKey="name"/>
                        <YAxis/>
                        <Tooltip/>
                        <Legend/>
                        <Bar dataKey="Pontuação" fill="#2C2C2C"/>
                    </BarChart>
                </ResponsiveContainer>
            </div>
            <div className="form-questionario">
                <button onClick={onResponderNovamente}>
                    Responder Novamente
                </button>
            </div>

            <div className="tecnicas-listagem">
                {tecnicas.map((t) => (
                    <Recomendacao tecnica={t}></Recomendacao>
                ))}
            </div>
        </div>
    );
}
