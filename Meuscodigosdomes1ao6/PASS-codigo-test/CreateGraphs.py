import numpy as np
import matplotlib.pyplot as plt
Title,lateralBar,DownBar = input("Title? "),input("Lateral bar ?: "),input("Down bar name?: ") 
cat1,cat2,cat3,cat4,cat5 = input("categora1: "),input("categora2: "),input("categora3: "),input("categora4: "),input("categora5: ")
Val1,Val2,Val3,Val4,Val5 = int(input("Digite o valor 1: ")),int(input("Digite o valor 2: ")),int(input("Digite o valor 3: ")),int(input("Digite o valor 4: ")),int(input("Digite o valor 5: "))
val1,val2,val3,val4,val5 = int(input("Digite o valor 1: ")),int(input("Digite o valor 2: ")),int(input("Digite o valor 3: ")),int(input("Digite o valor 4: ")),int(input("Digite o valor 5: "))
categorias = [cat1, cat2, cat3, cat4, cat5,]
valores_yes = [Val1, Val2, Val3, Val4, Val5]
valores_no = [val1, val2, val3, val4, val5]
x = np.arange(len(categorias))
largura_barra = 0.35
fig, ax = plt.subplots()
barras_yes = ax.bar(x - largura_barra/2, valores_yes, largura_barra, label='Yes')
barras_no = ax.bar(x + largura_barra/2, valores_no, largura_barra, label='No')
ax.set_title(Title)
ax.set_xlabel(DownBar)
ax.set_ylabel(lateralBar)
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend()
def autolabel(barras):
    for barra in barras:
        altura = barra.get_height()
        ax.annotate('{}'.format(altura),
                    xy=(barra.get_x() + barra.get_width() / 2, altura),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(barras_yes)
autolabel(barras_no)
plt.show()