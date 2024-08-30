ops = input("\n____________\nQuantidade de Subconjunto(OBS:se escrever somente subconjunto também vai)\nAuB\nAnB\ncomplemento\nDigite qual conjunto desejá: ")
if ops.lower() == 'Quantidade de Subconjunto' or ops.lower() == 'subconjunto':
    opsc1 = int(input("Desejá quantos elementos? "))
    A = set()
    for i in range(opsc1):
        save1 = int(input("Digite o elemento que deseja: "))
        A.add(save1)
    subconjunte= len(A)
    print(f"A={A}\nQuantidade de subconjunto = 2**{subconjunte} = {2**subconjunte}")
elif ops.lower() == 'aub':
    CAbc = input("_____________\nAuB ou AuBuC\nQual união desejá: ")
    if CAbc == 'aub':
        opsc1 = int(input("Desejá quantos elementos no  conunto A? "))
        A = set()
        for i in range(opsc1):
            save1 = int(input("Digite o elemento que deseja: "))
            A.add(save1)
        opsc2 = int(input("Desejá quantos elementos no conjunto B? "))
        B = set()
        for i in range(opsc2):
            save2 = int(input("Digite o elemento que deseja: "))
            B.add(save2)
        R = A.union(B)
        print(R)
    elif CAbc == 'aubuc':
        opsc1 = int(input("Desejá quantos elementos no  conunto A? "))
        A = set()
        for i in range(opsc1):
            save1 = int(input("Digite o elemento que deseja: "))
            A.add(save1)
        opsc2 = int(input("Desejá quantos elementos no conjunto B? "))
        B = set()
        for i in range(opsc2):
            save2 = int(input("Digite o elemento que deseja: "))
            B.add(save2)
        opsc3 = int(input("Desejá quantos elementos no conjunto C? "))
        C = set()
        for i in range(opsc3):
            save3 = int(input("Digite o elemento que deseja: "))
            C.add(save3)
        R = A.union(B and C)
        print(R)
elif ops.lower() == 'anb':
    CAbc = input("_____________\nAuB ou AuBuC\nQual união desejá: ")
    if CAbc == 'anb':
        opsc1 = int(input("Desejá quantos elementos no  conujunto A? "))
        A = set()
        for i in range(opsc1):
            save1 = int(input("Digite o elemento que deseja: "))
            A.add(save1)
        opsc2 = int(input("Desejá quantos elementos no conjunto B? "))
        B = set()
        for i in range(opsc2):
            save2 = int(input("Digite o elemento que deseja: "))
            B.add(save2)
        R = A.intersection(B)
        print(R)
    elif CAbc == 'anbnc':
        opsc1 = int(input("Desejá quantos elementos no  conujunto A? "))
        A = set()
        for i in range(opsc1):
            save1 = int(input("Digite o elemento que deseja: "))
            A.add(save1)
        opsc2 = int(input("Desejá quantos elementos no conjunto B? "))
        B = set()
        for i in range(opsc2):
            save2 = int(input("Digite o elemento que deseja: "))
            B.add(save2)
        opsc3 = int(input("Desejá quantos elementos no conjunto C? "))
        C = set()
        for i in range(opsc3):
            save3 = int(input("Digite o elemento que deseja: "))
            C.add(save3)
        R = A.intersection(B and C)
        print(R)
elif ops.lower() == 'complemento':
    TypeC = input("__________________\nAeB\nBeC\nAeC\nQuer fazer complemento com quais conjuntos? ")
    if TypeC.lower() == 'aeb':
        opsc1 = int(input("Desejá quantos elementos no conjunto A? "))
        A = set()
        for i in range(opsc1):
            save1 = int(input("Digite o elemento que deseja: "))
            A.add(save1)
        opsc2 = int(input("Desejá quantos elementos no conjunto B? "))
        B = set()
        for i in range(opsc2):
            save2 = int(input("Digite o elemento que deseja: "))
            B.add(save2)
        print(f"A = {sorted(A)}\nB = {sorted(B)}\nO complemento é {sorted(A - B)}")
    elif TypeC.lower() == 'bec':
        opsc1 = int(input("Desejá quantos elementos no conjunto A? "))
        B = set()
        for i in range(opsc1):
            save1 = int(input("Digite o elemento que deseja: "))
            B.add(save1)
        opsc2 = int(input("Desejá quantos elementos no conjunto B? "))
        C = set()
        for i in range(opsc2):
            save2 = int(input("Digite o elemento que deseja: "))
            B.add(save2)
        print(f"A = {sorted(B)}\nB = {sorted(C)}\nO complemento é {sorted(B - C)}")
    elif TypeC.lower() == 'aec':
        opsc1 = int(input("Desejá quantos elementos no conjunto A? "))
        A = set()
        for i in range(opsc1):
            save1 = int(input("Digite o elemento que deseja: "))
            A.add(save1)
        opsc2 = int(input("Desejá quantos elementos no conjunto B? "))
        C = set()
        for i in range(opsc2):
            save2 = int(input("Digite o elemento que deseja: "))
            C.add(save2)
        print(f"A = {sorted(A)}\nB = {sorted(C)}\nO complemento é {sorted(A - C)}")