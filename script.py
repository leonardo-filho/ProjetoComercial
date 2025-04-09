# Este projeto Power BI utiliza scripts em Python para transformação de dados.
# Este arquivo é usado para indicar o uso da linguagem no repositório.

import pandas as pd

# Exemplo genérico de carregamento e pré-processamento de dados
df = pd.read_csv("dados.csv")
df["coluna"] = df["coluna"].fillna(0)
print(df.head())
