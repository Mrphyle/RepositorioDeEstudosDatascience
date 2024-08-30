operation = input("Type '1' for the first power, '2' for the third power, '4' for the fourth power, and '5'.\n'Equação'.\n Or 'op1=+' 'op2= -' 'op3=*' 'op4=/' = ")
if operation == '1':
    base1 = float(input('A primeira base é = '))
    exponent1 = float(input('O primeiro expoente vai ser = '))
    base2 = float(input("A segunda base será = "))
    exponent2 = float(input('O segundo exponte será = '))
    result1 = float(base1) ** float(exponent1)
    result2 = float(base2) ** float(exponent2)
    result3 = float(result1) * float(result2)
    print(result1,"*",result2,"=",result3)
    print("Resposta=",result3)
elif operation == '2':
    base1 = float(input('A primeira base é = '))
    exponent1 = float(input('O primeiro expoente vai ser = '))
    base2 = float(input("A segunda base será = "))
    exponent2 = float(input('O segundo exponte será = '))
    result1 = base1 ** exponent1
    result2 = base2 ** exponent2
    result3 = result1 / result2
    print('potence1 =', result1)
    print('potence2=',result2)
    print(result1,"/",result2,"=",result3)
elif operation == '3':
    base1 = float(input('Qual o valor da primeira Base = '))
    base2 = float(input('Qual o valor da segunda base = '))
    exponent = float(input('Qual o valor do expoente = '))
    result1 = float(base1) ** float(exponent)
    result2 = float(base2) ** float(exponent)
    result3 = float(result1) * float(result2)
    print('(',base1,'*',base2,')','**',exponent)
    print(result1,'*',result2,'=',result3)
    print('Resposta=',result3)
elif operation == '4':
    base = float(input('Digite a base = '))
    exponent1 = float(input('Digite o primeiro expoente = '))
    exponent2 = float(input('Digite o segundo exponent = '))
    result1 = float(exponent1) * float(exponent2)
    result2 = float(base) ** float(result1)
    print('(',base,'**',exponent1,')','**',exponent2)
    print(base,'**',exponent1,'*',exponent2)
    print(base,'**',result1)
    print('Resultado=',result2)
elif operation == 'op1':
    result01 = input("Type number1= ")
    result02 = input("Type number2= ")
    result03 = float(result01) + float(result02)
    print(result01,'+',result02,'=',result03)
elif operation == 'op2':
    result01 = input("Type number1= ")
    result02 = input("Type number2= ")
    result03 = float(result01) - float(result02)
    print(result01,'-',result02,'=',result03)
elif operation == 'op3':
    result01 = input("Type number1= ")
    result02 = input("Type number2= ")
    result03 = float(result01) * float(result02)
    print(result01,'*',result02,'=',result03)
elif operation == 'op4':
    result01 = input("Type number1= ")
    result02 = input("Type number2= ")
    result03 = float(result01) / float(result02)
    print(result01,'/',result02,'=',result03)
elif operation == 'Equação':
    a = float(input('coloque o X*2 que é = '))
    b = float(input ('coloque o X que é = '))
    c = float(input('Coloque o numero que é representado pelo c = '))
    result1 = float(b) ** 2
    print("Delta=", result1,'-','4','*',a,'*',c )
    Delta = float(result1) - 4 * float(a) * float(c)
    print('Delta=', Delta)
    raiz_Delta = Delta **0.5
    print('raiz de Delta=', raiz_Delta)
    x1 = float(-b) - float(raiz_Delta)
    x2 = float(- b) + float(raiz_Delta)
    result2 = 2 * a 
    print(-b,'+-', Delta, '/2 *', a)
    print('x1=',-b,'-', raiz_Delta,'=', x1,'/', result2)
    print('x2=',-b,'+',raiz_Delta,'=', x2,'/', result2)