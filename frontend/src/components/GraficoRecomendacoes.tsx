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

export function GraficoRecomendacoes({tecnicas}) {
    return (
        <div className="grafico-tecnicas" style={{}}>
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
    );
}