import React, { createContext, useContext, useEffect, useState } from "react";
import { getVendedores } from "../services/Vendedor.service";

const VendedorContext = createContext([]);

const VendedorProvider = ({children}) => {

    const [vendedores, setVendedores] = useState([])
    async function loadVendedores() {
        let vendedores = await getVendedores()
        setVendedores(vendedores.data)
    }

    return (
        <VendedorContext.Provider value={{ vendedores, setVendedores, loadVendedores }}>
            {children}
        </VendedorContext.Provider>
    )

}

function useVendedoresContext() {
    const context = useContext(VendedorContext);
    if(!context) throw new Error('Not inside the Provider')
    return context
}



export {VendedorContext, VendedorProvider, useVendedoresContext}