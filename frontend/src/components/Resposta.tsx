type RespostaProsps = {
    resposta: any;
    checked: boolean;
    onSelect: () => void;
};

export function Resposta({resposta, checked, onSelect}: RespostaProsps) {
    return (
        <label className="resposta">
            <input
                type="radio"
                checked={checked}
                onChange={onSelect}
            />
            {resposta.conteudo}
        </label>
    );
}
