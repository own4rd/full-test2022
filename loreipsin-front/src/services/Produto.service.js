
import api from './api'

export const buscarProdutos = async (filtro) => {
    return await api.get(`itens/?search=${filtro}`)
};
