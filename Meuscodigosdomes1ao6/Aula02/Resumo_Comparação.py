opção = input("Digite 'comp1' ou 'comp2' ou 'comp3'= ")
if opção == 'comp1':
    n1 = float(input("Digite o numero"))
    n2 = float(input("Digite o numero"))
    if (n1>n2):
        print("sim,",n1,'maior do que',n2)
    if (n2>n1):
        print("sim,",n2,'maior do que',n1)
    if (n2==n1):
        print("sim,",n1,'é igual do que',n2)  
elif opção == 'comp2':
    ano_nacimento = int(input("ano de nascimento= "))
    ano_atual = 2024
    idade = ano_atual - ano_nacimento
    if (idade>=18):
        print('Parabens, vc está contratado')
    else:
        print("Reprovado volte quando tiver 18+")
elif opção == 'comp3':
    saldo = float(input('quanto é seu saldo?= '))
    saque = float(input('quanto quer sacar?= '))
    if saldo >= saque:
        resto = saldo - saque
        print('Pode retirar o dinheiro você tem o sulficiente','sobrou R$',resto,'em sua conta')
    else:
        print('Seu saldo não é o sulficiente')