import './Table.css'

const Table = (props) => {
    const {textsHead, textsContent} = props
    return(
        <table>
            <thead>
                <tr>
                    {textsHead.map(text => <th key={text}>{text}</th>)}
                </tr>
            </thead>
            <tbody>
                {textsContent.map(content => (
                <tr key={content.item}>
                    <td>{content.nome}</td>
                    <td>{content.quantidade}</td>
                    <td>R$ {content.preco}</td>
                    <td>R$ {content.total}</td>
                    <td onClick={() => props.removeItem(content.id)}><i className="fas fa-trash"></i></td>
                </tr>
                ))}
            </tbody>
        </table>
    )
}

export default Table