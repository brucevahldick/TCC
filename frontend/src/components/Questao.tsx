import {Resposta} from "./Resposta";

type QuestaoProps = {
    questao: any;
    respostaSelecionada: any;
    onSelect: (questao_id: any, resposta_id: any) => void;
};

export function Questao({questao, respostaSelecionada, onSelect}: QuestaoProps) {
    return (
        <div className="questao-container">
            <div className="questao">
                {questao.codigo} - {questao.conteudo}
            </div>
            <div className="resposta-container">
                {questao.respostas.map((r: any) => (
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
