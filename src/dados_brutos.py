import pandas as pd

tabela = pd.read_csv('data/vendas.csv')
#print(tabela)

# padronizacao das colunas
tabela.columns = tabela.columns.str.strip().str.lower()

# remover colunas vazias
tabela = tabela.dropna(axis=1, how='all')
print(tabela)

# tipos de dados
print(tabela.info())