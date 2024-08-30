import os
def MaisMenosVezesDividir():
    opcao = input("\n_____________\nSomar\nSubtrair\nDividir\nMultiplicar\nPotencia\nO que deseja fazer? ")
    if opcao.lower() == 'somar':
        def som():
            num1, num2 = float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: "))
            print(f"{num1} + {num2} = {num1 + num2}")
        while True:
            som()
            rescont = input("Deseja fazer outra soma? ")
            if not rescont.lower() in ['sim','yes','1']:
                print("\n")
                break
    elif opcao.lower() == 'subtrair':
        def sub():
            num1, num2 = float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: "))
            print(f"{num1} - {num2} = {num1 - num2}")
        while True:
            sub()
            rescont = input("Deseja fazer outra subtração? ")
            if not rescont.lower() in ['sim','yes','1']:
                print("\n")
                break
    elif opcao.lower() == 'dividir':
        def div():
            num1, num2 = float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: "))
            print(f"{num1} / {num2} = {num1 / num2}")
        while True:
            div()
            rescont = input("Deseja fazer outra conta de divisão? ")
            if not rescont.lower() in ['sim','yes','1']:
                print("\n")
                break
    elif opcao.lower() == 'multiplicar':
        def mult():
            num1, num2 = float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: "))
            print(f"{num1} * {num2} = {num1 * num2}")
        while True:
            mult()
            rescont = input("Deseja fazer outra multiplicação? ")
            if not rescont.lower() in ['sim','yes','1']:
                print("\n")
                break    
    else:
        def potence():
            num1, num2 = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))
            print(f"{num1} **{num2} = {num1**num2}")    
        while True:
            potence()
            rescont = input("Deseja fazer outra potencia? ")
            if not rescont.lower() in ['sim','yes','1']:
                print("\n")
                break
while True:
    MaisMenosVezesDividir()
    Del = input("Desejá deletar o que já foi feito?")
    reset = input("Quer fazer outra operação? ") 
    if Del.lower() in ['sim','yes','1']:
        os.system('cls' if os.name == 'nt' else 'clear')
    if not reset.lower() in ['sim','yes','1']:
        print('__________________\ncomando Finalizado!')
        break