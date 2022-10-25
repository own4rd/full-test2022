import React, { createContext, useContext, useState } from "react";

const ProdutoContext = createContext([]);

const ProdutoProvider = ({children}) => {

    const [produtos, setProdutos] = useState([])

    async function updateProdutosSearch(buscaValue) {
        await fetch(`http://localhost:8000/api/itens/?search=${buscaValue}`)
        .then(response => response.json())
        .then(data => setProdutos(data));
    }

    return (
        <ProdutoContext.Provider value={{ produtos, setProdutos, updateProdutosSearch }}>
            {children}
        </ProdutoContext.Provider>
    )

}

function useProdutosSearch() {
    const context = useContext(ProdutoContext);
    if(!context) throw new Error('Not inside the Provider')
    return context
}



export {ProdutoContext, ProdutoProvider, useProdutosSearch}