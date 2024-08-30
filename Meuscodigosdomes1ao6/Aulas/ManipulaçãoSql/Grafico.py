'''import matplotlib.pyplot as plt
X = [10, 15, 30, 45]
colors = ['blue', 'green', 'red', 'orange']
plt.title("Gráfico de Pizza")
plt.figure(figsize=(6, 6))
plt.pie(X, colors=colors)
plt.show()
'''
import matplotlib.pyplot as plt
import numpy as np
X = [10, 15, 30, 45]
colors = ['blue', 'green', 'red', 'orange']
plt.title("Gráfico de Pizza")
plt.figure(figsize=(6, 6))
def absolute_value(val):
    total = np.sum(X)
    return int(val / 100. * total)
plt.pie(X, colors=colors, autopct=lambda val: absolute_value(val))
plt.show()