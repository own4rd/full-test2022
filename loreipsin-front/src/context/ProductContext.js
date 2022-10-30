import React, { createContext, useContext, useState } from "react";
import { buscarProdutos } from "../services/Produto.service";

const ProdutoContext = createContext([]);

const ProdutoProvider = ({children}) => {

    const [produtos, setProdutos] = useState([])

    // Hook customizado
    async function updateProdutosSearch(buscaValue) {
        let produtos_search = await buscarProdutos(buscaValue);
        setProdutos(produtos_search.data);
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