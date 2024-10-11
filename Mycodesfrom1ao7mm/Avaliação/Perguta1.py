a = float(input('coloque o ax**2 que é = '))
b = float(input('coloque o bX que é = '))
c = float(input('Coloque o c = '))
result1 = b ** 2
Delta = result1 - 4 * a * c
if (Delta < 0):
    print('Sem raízes reais')
if (Delta == 0):
    print('Delta é igual a zero, portanto não é possível fazer Bhaskara')
if (Delta > 0):
    raizDelta = Delta ** 0.5
    x1 = -b - raizDelta
    x2 = -b + raizDelta
    result2 = 2 * a 
    print('x1 =', -b, '-', raizDelta, '=', x1, '/', result2)
    print('x2 =', -b, '+', raizDelta, '=', x2, '/', result2)