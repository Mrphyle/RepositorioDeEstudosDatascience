import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/home/mrphyle/Documents/RepositorioDeEstudosDatascience/2026 files/python/vendas.csv')
df['data'] = pd.to_datetime(df['data'])
df['Valor_Total'] = df['quantidade'] * df['valor_unitario']
maior_venda = df['Valor_Total'].max()
menor_venda = df['Valor_Total'].min()
media_venda = df['Valor_Total'].mean()
mediana_venda = df['Valor_Total'].median()

Ranking_vendas = (df.groupby('produto')['Valor_Total'].sum().sort_values(ascending=False))
print(f"\n-------Medidas--------\nMaior venda: {maior_venda:.2f}\nMenor venda: {menor_venda:.2f}\nMédia de vendas: {media_venda:.2f}\nMediana de vendas: {mediana_venda:.2f}")
print(f"\n-------Ranking--------\n{Ranking_vendas}")

plt.figure(figsize=(10, 6))
Ranking_vendas.plot(kind='bar')
plt.title('Ranking de Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Valor Total de Vendas')
plt.tight_layout()
plt.show()