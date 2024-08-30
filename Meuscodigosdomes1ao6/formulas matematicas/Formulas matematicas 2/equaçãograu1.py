import math

# Coeficientes da equação quadrática
a = 2
b = 4
c = 5

# Calculando o discriminante
delta = b**2 - 4*a*c

print("Passo 1: Calculando o discriminante (Delta):")
print("Delta = b^2 - 4ac")
print("Delta =", b, "^2 - 4 *", a, "*", c)
print("Delta =", delta)
print()

# Verificando se o discriminante é zero
if delta == 0:
    print("O discriminante é zero. A equação tem raízes iguais.")
    print("Passo 2: Usando a fórmula de Bhaskara para encontrar as raízes:")
    x = -b / (2*a)
    print("x =", x)
else:
    print("O discriminante não é zero. A equação não tem raízes iguais.")