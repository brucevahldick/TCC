import {Resposta} from "./Resposta";

export function Questao({questao, respostaSelecionada, onSelect}) {
    return (
        <div className="questao-container">
            <div className="questao">
                {questao.codigo} - {questao.conteudo}
            </div>
            <div className="resposta-container">
                {questao.respostas.map((r) => (
                    <Resposta
                        key={r.id}
                        resposta={r}
                        checked={respostaSelecionada === r.id}
                        onSelect={() => onSelect(questao.id, r.id)}
                    />
                ))}
            </div>
        </div>
    );
}
