import streamlit as st
import pandas as pd

tabela = pd.read_csv('data/vendas.csv')

st.title('Análise de Vendas')

regioes = st.multiselect("Selecione as regiões", tabela['Regiao'].unique())

if regioes:
    tabela = tabela[tabela['Regiao'].isin(regioes)]

st.metric("Total de Vendas", f"R$ {tabela['ValorVenda'].sum():,.2f}")
st.metric("Ticket Médio", f"R$ {tabela['ValorVenda'].mean():,.2f}")

st.bar_chart(tabela.groupby('Regiao')['ValorVenda'].sum())
st.bar_chart(tabela.groupby('Produto')['ValorVenda'].sum())