import React, { createContext, useContext, useEffect, useState } from "react";

const ClienteContext = createContext([]);

const ClienteProvider = ({children}) => {

    const [clientes, setClientes] = useState([])
    async function loadClientes() {
        await fetch(`http://localhost:8000/api/clientes/`)
        .then(response => response.json())
        .then(data => setClientes(data));
    }

    return (
        <ClienteContext.Provider value={{ clientes, setClientes, loadClientes }}>
            {children}
        </ClienteContext.Provider>
    )

}

function useClienteContext() {
    const context = useContext(ClienteContext);
    if(!context) throw new Error('Not inside the Provider')
    return context
}



export {ClienteContext, ClienteProvider, useClienteContext}