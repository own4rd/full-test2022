import './InputText.css'

const InputText = (props) => {
    return(
        <div className={props.classes}>
            <div className="autocomplete">
                <label htmlFor={props.name}>{props.label}</label>
                <input onChange={props.onChange} type={props.type} id={props.name} name={props.name} className='form-control' value={props.valor} placeholder={props.placeholder}/>
                {props.autoSuggest ?
                <ul className="list">
                    {props.arraySearch.map(produto => (
                        <li key={produto.id} className="list-items" onClick={() => props.onSelectItem(produto)}> {produto.id} - {produto.nome}</li>
                    ))}
                </ul>
                : null}

            </div>
        </div>
    )
}

export default InputText