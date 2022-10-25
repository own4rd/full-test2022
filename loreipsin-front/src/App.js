import React, { useEffect, useState } from 'react';

import Button from "./components/Button";
import Header from "./components/Header";
import InputSelect from "./components/InputSelect";
import InputText from "./components/InputText";
import Table from "./components/Table";
import { useClienteContext } from './context/ClientesContext';
import { useProdutosSearch } from './context/ProductContext';
import { useVendaContext } from './context/VendaContext';
import { useVendedoresContext } from './context/VendedoresContext';



const inputInitialState = {
  'busca': '',
  'itensvenda': [],
  'quantidade': 0
}

function App() {
  const { produtos, setProdutos, updateProdutosSearch  } = useProdutosSearch();
  const { vendedores, loadVendedores } = useVendedoresContext();
  const { clientes, loadClientes } = useClienteContext();
  const { salvarVenda } = useVendaContext();

  const [inputs, setInputs] = useState(inputInitialState);
  const [produto, setProduto] = useState([]);
  const [selectedProdutos, setSelectedProdutos] = useState([]);
  const [message, setMessage] = useState([]);


  useEffect(() => {
    loadVendedores();
    loadClientes();
  }, [])

  var tableTextsHead = [
    "Produto/Serviço",
    "Quantidade",
    "Preço Unitário",
    "Total"
  ]

  const onChangeSearch = (e) => {
    e.preventDefault()
    setInputs(values => ({...values, 'busca': ''}))
    let buscaValue = e.target.value;
    if (buscaValue === ''){
      setProdutos([])
    } else {
      updateProdutosSearch(buscaValue)
      setInputs(values => ({...values, 'busca': buscaValue}))
    }
  }

  const onSelectItem = (produto) => {
    setInputs(values => ({...values, 'busca': produto.nome}))
    setProduto(produto)
    setProdutos([])
  }
    
  const onClickAddProduto = (e) => {
    e.preventDefault()
    if(inputs.quantidade <= 0) {
      setMessage({
        'info': 'Quantidade de itens deve ser maior que 0',
        'type': 'error'
      })
      return 
    }
    setSelectedProdutos([...selectedProdutos, {
      'item': produto.id,
      'nome': produto.nome,
      'preco': produto.preco,
      'quantidade': inputs.quantidade,
      'total': inputs.quantidade * produto.preco
    }])

    setInputs(values => ({...values, 'quantidade': 0}))
  }
  
  const onRemoveProduto = (id_produto) => {
    let newSelectedProdutos = selectedProdutos.filter(function(produto) {
      return produto.item !== id_produto
    })
    setSelectedProdutos(newSelectedProdutos)
  }

  const onSubmitForm = async (e) => {
    e.preventDefault()
    if(!inputs.vendedor || !inputs.cliente) {
      setMessage({
        'info': 'É necessário informar vendedor e cliente.',
        'type': 'error'
      })
      return 

    }
    let response = await salvarVenda(JSON.stringify({
      'itensvenda': selectedProdutos,
      'vendedor': inputs.vendedor,
      'cliente': inputs.cliente
    }))
    setMessage(response);
  } 

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}))
  }

  return (
    <div className="App">
      <Header />
      <form onSubmit={onSubmitForm}>
        <div className="container d-flex pt-5">
          <div className='col-12'>

          {
            message ? <div className={`msg-${message.type}`}>{message.info}</div>
            : null
          }
          </div>
          <div className="col-8 mr-3 divisor-panels pr-2">
            <h3 className="title-info">Produtos</h3>
            <div className="row d-flex">
                <div className="col-6 mr-3">
                  <InputText 
                    name="busca"
                    valor={inputs.busca} 
                    onSelectItem={onSelectItem} 
                    arraySearch={produtos} 
                    onChange={onChangeSearch} 
                    label="Buscar pelo código de barras ou descrição" 
                    autoSuggest={true} 
                    placeholder="Descricao" type="text" />
                </div>
                <div className="col-4 mr-3">
                  <InputText 
                    name="quantidade"
                    valor={inputs.quantidade}  
                    label="Quantidade de itens" 
                    onChange={handleChange} 
                    placeholder="0" type="number" />
                </div>
                <div className="col-3 mt-5 align-right">
                    <Button texto="Adicionar" onClick={onClickAddProduto} />
                </div>
                <div className="col-12 mt-5">
                  <Table textsHead={tableTextsHead} textsContent={selectedProdutos} removeItem={onRemoveProduto}/>
                </div>
            </div>
          </div>
          <div className="col-4" >
            <h3 className="title-info">Dados da venda</h3>
            <InputSelect name="vendedor" valor={inputs.vendedor} label="Escolha um vendedor" values={vendedores} handleChangeSelect={handleChange} />
            <InputSelect name="cliente" valor={inputs.cliente} label="Escolha um cliente" classes="pt-5" values={clientes} handleChangeSelect={handleChange}/>
            <div className="d-flex align-between" style={{marginTop: 130}}>
              <p className="font-bold">Valor total da venda</p>
              <p className="font-bold">R$ 
                {selectedProdutos.reduce((preco,produto) => preco=preco+produto.total, 0)}
              </p>
            </div>
            <div className="d-flex align-between" style={{marginTop: 20}}>
              <Button texto="Candelar"/>
              <Button texto="Finalizar" classes="btn-success"/>
            </div>
          </div>
        </div>
      </form>
    </div>
  );
}

export default App;
