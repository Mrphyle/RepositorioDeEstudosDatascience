a = float(input('coloque o X*2 que é = '))
b = float(input ('coloque o X que é = '))
c = float(input('Coloque o numero que é representado pelo c = '))
result1 = float(b) ** 2
print("Delta=", result1,'-','4','*',a,'*',c )
Delta = float(result1) - 4 * float(a) * float(c)
print('Delta=', Delta)
if (Delta < 0):
    print('Sem raízes reais')
if (Delta >= 0):
    raizDelt1 = Delta **0.5
    raizDelta2= round(raizDelt1,2)
    print('raiz de Delta=', raizDelta2)
    x1 = float(-b) - float(raizDelta2)
    x2 = float(- b) + float(raizDelta2)
    X1 = round(x1,1)
    X2 = round(x2,1)
    result2 = 2 * a 
    print(-b,'+-', Delta, '/2 *', a)
    print('x1=',-b,'-', raizDelta2,'=', X1,'/', result2)
    print('x2=',-b,'+',raizDelta2,'=', X2,'/', result2)