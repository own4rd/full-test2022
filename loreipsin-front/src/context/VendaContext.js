import React, { createContext, useContext } from "react";
import { cadastrarVenda } from "../services/Venda.service";

const VendaContext = createContext([]);

const VendaProvider = ({children}) => {
    async function salvarVenda(data) {
        let response = await cadastrarVenda(data)
        if (response.status === 201){
            return {'info': 'Venda cadastrada com sucesso.', 'type': 'success'}
        } else {
            return {'info': 'Erro ao cadastrar venda.', 'type': 'error'}
        }
    }

    return (
        <VendaContext.Provider value={{ salvarVenda }}>
            {children}
        </VendaContext.Provider>
    )

}

function useVendaContext() {
    const context = useContext(VendaContext);
    if(!context) throw new Error('Not inside the Provider')
    return context
}



export {VendaContext, VendaProvider, useVendaContext}