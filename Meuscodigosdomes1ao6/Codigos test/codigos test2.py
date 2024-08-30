def tipotriangulo():
    #define o tipo do triangulo
    l1= float(input("tamanho do primeiro lado: ")) 
    l2= float(input("tamanho do segundo lado: "))
    l3= float(input("tamanho do treceiro lado: "))
    if l1 == l2 == l3:
        print("O triangulo tem os três lados iguais\nO triangulo é Equilatero.")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("O triangulo tem dois lados iguais\nO triangulo é Isósceles")
    else:
        print("O triangulo não possui lado igual\nO triangulo é Escaleno")
#linha 2 e 12 até 16 faz o reset do codigo.
while True:
    tipotriangulo()
    triangulorestart = input("quer verificar outro triangulo? ")
    if triangulorestart.lower() != 'sim':
        break