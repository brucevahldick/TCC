export function Resposta({ resposta, checked, onSelect }) {
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
