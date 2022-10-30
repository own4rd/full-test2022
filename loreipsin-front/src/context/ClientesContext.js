import React, { createContext, useContext, useEffect, useState } from "react";
import { getClientes } from "../services/Cliente.service";

const ClienteContext = createContext([]);

const ClienteProvider = ({children}) => {

    const [clientes, setClientes] = useState([])
    async function loadClientes() {
        let clientes = await getClientes();
        setClientes(clientes.data);
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