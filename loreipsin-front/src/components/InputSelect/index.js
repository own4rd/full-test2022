import './InputSelect.css'

const InputSelect = (props) => {
    return(
        <div className={props.classes}>
            <label>{props.label}</label>
            <select name={props.name} className="form-control" value={props.valor?.id} onChange={props.handleChangeSelect}>
                <option key="-1">-------------</option>
                {props.values.map((data) => <option value={data.id} key={data.id}>{data.nome}</option>)}
            </select>
        </div>
    )
}

export default InputSelect