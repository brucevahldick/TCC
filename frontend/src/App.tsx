import { useState, useEffect } from "react";
import "./App.scss";

interface Resposta {
    id: number;
    conteudo: string;
}

interface Questao {
    id: number;
    codigo: string;
    conteudo: string;
    respostas: Resposta[];
}

interface Tecnica {
    id: number;
    codigo: string;
    nome: string;
    pontuacao_total: number;
}

function App() {
    const apiUrl = import.meta.env.VITE_API_URL || "http://localhost:8000";
    const [questoes, setQuestoes] = useState<Questao[]>([]);
    const [respostasSelecionadas, setRespostasSelecionadas] = useState<{ [key: number]: number }>({});
    const [recomendacoes, setRecomendacoes] = useState<Tecnica[]>([]);
    const [loading, setLoading] = useState(false);
    const [erro, setErro] = useState<string | null>(null);

    // Busca as questões e respostas do backend
    useEffect(() => {
        const fetchQuestoes = async () => {
            try {
                const res = await fetch(`${apiUrl}/`);
                if (!res.ok) throw new Error(`Erro ao buscar questões: ${res.status}`);
                const data = await res.json();
                setQuestoes(data.questoes || []);
            } catch (err) {
                setErro(err instanceof Error ? err.message : "Erro desconhecido");
            }
        };

        fetchQuestoes();
    }, [apiUrl]);

    // Atualiza a resposta selecionada
    const handleSelectResposta = (questaoId: number, respostaId: number) => {
        setRespostasSelecionadas((prev) => ({ ...prev, [questaoId]: respostaId }));
    };

    // Envia respostas para obter recomendação
    const handleSubmit = async () => {
        const respostas = Object.values(respostasSelecionadas);
        if (respostas.length === 0) {
            alert("Selecione ao menos uma resposta antes de enviar.");
            return;
        }

        setLoading(true);
        setErro(null);

        try {
            const res = await fetch(`${apiUrl}/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ respostas }),
            });

            if (!res.ok) throw new Error(`Erro HTTP ${res.status}`);
            const data = await res.json();
            setRecomendacoes(data.tecnicas || []);
        } catch (err) {
            setErro(err instanceof Error ? err.message : "Erro desconhecido");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="app-container">
            <h1>Questionário de Técnicas Recomendadas</h1>

            {erro && <p className="erro">❌ {erro}</p>}

            {questoes.length === 0 && !erro && <p>Carregando questões...</p>}

            {questoes.map((q) => (
                <div key={q.id} className="questao">
                    <h3>
                        {q.codigo} - {q.conteudo}
                    </h3>
                    {q.respostas.map((r) => (
                        <label key={r.id} className="resposta">
                            <input
                                type="radio"
                                name={`questao-${q.id}`}
                                value={r.id}
                                checked={respostasSelecionadas[q.id] === r.id}
                                onChange={() => handleSelectResposta(q.id, r.id)}
                            />
                            {r.conteudo}
                        </label>
                    ))}
                </div>
            ))}

            <button onClick={handleSubmit} disabled={loading || questoes.length === 0}>
                {loading ? "Enviando..." : "Enviar Respostas"}
            </button>

            {recomendacoes.length > 0 && (
                <div className="recomendacoes">
                    <h2>Recomendações de Técnicas</h2>
                    <ul>
                        {recomendacoes.map((t) => (
                            <li key={t.id}>
                                <strong>{t.nome}</strong> ({t.codigo}) — Pontuação:{" "}
                                {t.pontuacao_total.toFixed(2)}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default App;
