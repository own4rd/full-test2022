
import api from './api'

export const getClientes = async () => {
    return await api.get(`clientes/`)
};
