import './Button.css'

const Button = (props) => {
    return(
        <button onClick={props.onClick} className={props.classes}>{props.texto}</button>
    )
}

export default Button