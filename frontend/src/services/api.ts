// @ts-ignore
const apiUrl = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function getQuestoes() {
    const res = await fetch(`${apiUrl}/`);
    if (!res.ok) throw new Error(`Erro ao buscar questões: ${res.status}`);
    return res.json();
}

export async function postRespostas(respostas: number[]) {
    const res = await fetch(`${apiUrl}/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ respostas }),
    });
    if (!res.ok) throw new Error(`Erro HTTP ${res.status}`);
    return res.json();
}
