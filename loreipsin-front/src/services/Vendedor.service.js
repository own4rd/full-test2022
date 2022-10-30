
import api from './api'

export const getVendedores = async () => {
    return await api.get(`vendedores/`)
};
