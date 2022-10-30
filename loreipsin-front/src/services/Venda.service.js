
import api from './api'

export const cadastrarVenda = async (venda) => {
    return await api.post(`vendas/`, venda)
};
