import React, { createContext, useContext, useEffect, useState } from "react";

const VendedorContext = createContext([]);

const VendedorProvider = ({children}) => {

    const [vendedores, setVendedores] = useState([])
    async function loadVendedores() {
        await fetch(`http://localhost:8000/api/vendedores/`)
        .then(response => response.json())
        .then(data => setVendedores(data));
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