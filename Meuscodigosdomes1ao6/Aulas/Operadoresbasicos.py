def mais_menos_vezes_Divisao():
    opcao = input("Somar\nSubtrair\nDividir\nMultiplicar\nO que deseja fazer? ")
    if opcao.lower() == 'somar':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif opcao.lower() == 'subtrair':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif opcao.lower() == 'dividir':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 == 0:
            print("Erro! Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
    elif opcao.lower() == 'multiplicar':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
while True:
    mais_menos_vezes_Divisao()
    reset = input("Quer fazer outra operação? (Sim/Não): ")
    if reset.lower() != 'sim':
        break