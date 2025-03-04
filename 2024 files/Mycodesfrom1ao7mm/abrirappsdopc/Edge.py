#Solicitar quantidade de minutos
TotalMinutos = float(input("Digite a quantidade de minnutos "))
#

Horas = TotalMinutos // 60
Minutos = TotalMinutos % 60
print(f"São {Horas}h{Minutos}mn")