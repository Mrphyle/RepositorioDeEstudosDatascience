import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('vendas.csv')
df['Valor_venda'] = df['Quantidade'] * df['Valor Unitário']
print(df)
vendatotal = df['Valor_venda'].sum()
print(f"Venda total: {vendatotal:.2f}")