'''import matplotlib.pyplot as plt

# Dados
gases = ['Hélio', 'Hidrogênio', 'Ar', 'Dióxido de Carbono']
min_tempo = [6, 6, 48, 72]
max_tempo = [12, 12, 72, 120]

# Criação do gráfico de barras
fig, ax = plt.subplots()

# Adicionando barras para o tempo mínimo e máximo
ax.bar(gases, min_tempo, label='Tempo Mínimo (horas)', color='blue', alpha=0.6)
ax.bar(gases, max_tempo, label='Tempo Máximo (horas)', color='red', alpha=0.6)

# Adicionando rótulos e título
ax.set_xlabel('Gás')
ax.set_ylabel('Taxa de Esvaziamento (horas)')
ax.set_title('Taxa de Esvaziamento de Balões com Diferentes Gases')
ax.legend()

# Exibindo o gráfico
plt.show()'''
import matplotlib.pyplot as plt
import numpy as np

# Dados dos gases e tempos de esvaziamento em condições normais (20°C)
gases = ['Hélio', 'Hidrogênio', 'Ar', 'Dióxido de Carbono']
min_tempo = np.array([6, 6, 48, 72])  # Tempo mínimo em horas
max_tempo = np.array([12, 12, 72, 120])  # Tempo máximo em horas

# Suposição de que o aumento da temperatura em 10°C aumenta a taxa de vazamento em 5%
temp_influence = 0.05  # 5% de aumento por 10°C
temperaturas = [20, 30, 40]  # Temperaturas em °C para comparar

# Função para calcular novos tempos baseados na temperatura
def calcular_tempo(tempo_inicial, temp_atual, temp_ref=20):
    aumento = (temp_atual - temp_ref) // 10 * temp_influence
    return tempo_inicial * (1 - aumento)

# Criar o gráfico
fig, ax = plt.subplots(figsize=(10, 6))

for temp in temperaturas:
    # Calcular novos tempos para cada temperatura
    min_tempo_temp = calcular_tempo(min_tempo, temp)
    max_tempo_temp = calcular_tempo(max_tempo, temp)
    
    # Adicionar barras para o tempo mínimo e máximo
    ax.bar(np.arange(len(gases)) - 0.2 + (temp - 20)/40, min_tempo_temp, width=0.2, label=f'Mínimo - {temp}°C')
    ax.bar(np.arange(len(gases)) + 0.2 + (temp - 20)/40, max_tempo_temp, width=0.2, label=f'Máximo - {temp}°C')

# Adicionando rótulos e título
ax.set_xlabel('Gás')
ax.set_ylabel('Taxa de Esvaziamento (horas)')
ax.set_title('Taxa de Esvaziamento de Balões com Diferentes Gases e Temperaturas')
ax.set_xticks(np.arange(len(gases)))
ax.set_xticklabels(gases)
ax.legend()

# Exibir o gráfico
plt.show()