import React from 'react';
import ReactDOM from 'react-dom/client';
import '@fortawesome/fontawesome-free/css/all.min.css';
import './index.css';
import App from './App';
import { ProdutoProvider } from './context/ProductContext';
import { VendedorProvider } from './context/VendedoresContext';
import { ClienteProvider } from './context/ClientesContext';
import { VendaProvider } from './context/VendaContext';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <ProdutoProvider>
      <VendedorProvider>
        <ClienteProvider>
            <VendaProvider>
              <App />
            </VendaProvider>
        </ClienteProvider>
      </VendedorProvider>
    </ProdutoProvider>
);
