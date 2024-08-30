'''Os números que compõem a potência são:
Base: O número que está sendo elevado a uma potência.
Expoente: O número que indica quantas vezes a base é multiplicada por si mesma.
Por exemplo, na potência 2 elevado a 3 
 , 2 é a base e 3 é o expoente.'''

base1 = float(input('A primeira base é = '))
exponent1 = float(input('O primeiro expoente vai ser = '))
base2 = float(input("A segunda base será = "))
exponent2 = float(input('O segundo exponte será = '))
result1 = float(base1) ** float(exponent1)
result2 = float(base2) ** float(exponent2)
result3 = float(result1) * float(result2)
print(result1,"*",result2,"=",result3)
print("Resposta=",result3)