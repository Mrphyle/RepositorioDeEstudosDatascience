import os
def codereset():
    ops = input("subjuntos\nAub\nAnb\ncomplemento\nQual deseja das opições? ")
    if ops.lower() == 'subconjunto':
        def subconjunto():
            ops1 = int(input("Desejá quantos elementos? "))
            A = set()
            for i in range(ops1):
                save = int(input("Digite o elemento: "))
                A.add(save)
            Subconjunto = len(A)
            print(f"{A}\nQuantindade de subconjunto é igual 2**{Subconjunto} ={2**Subconjunto}")
        while True:
            subconjunto()
            restcont = input("Deseja realizar a conta novamente? ")
            if not restcont.lower() in ['sim','yes','1']:
                break
    elif ops.lower() == 'aub':
        def AUB():    
            typeaub = input("AuB ou AuBuC\nDesejá fazer qual das opiçoes a cima? ")
            if typeaub.lower() == 'aub':
                ops1 = int(input("Desejá quantos elementos? "))
                A = set()
                for i in range(ops1):
                    save1 = int(input("Digite o elemento: "))
                    A.add(save1)
                ops2 = int(input("Desejá quantos elementos? "))
                B = set()
                for i in range(ops2):
                    save2 = int(input("Digite o elemento: "))
                    B.add(save2)
                print(f"A= {A}\nB={B}\nAUB={A.union(B)}")
            elif typeaub.lower() == 'aubuc':
                ops1 = int(input("Desejá quantos elementos? "))
                A = set()
                for i in range(ops1):
                    save1 = int(input("Digite o elemento: "))
                    A.add(save1)
                ops2 = int(input("Desejá quantos elementos? "))
                B = set()
                for i in range(ops2):
                    save2 = int(input("Digite o elemento: "))
                    B.add(save2)
                C = set()
                ops3 = int(input("Desejá quantos elementos? "))
                for i in range(ops3):
                    save3 = int(input("Digite o elemento: "))
                    C.add(save3)
                print(f"A= {A}\nB={B}\nC={C}\nAUB={A.union(B and C)}")
        while True:
            AUB()
            restcont = input("Deseja realizar a conta novamente? ")
            if not restcont.lower() in ['sim','yes','1']:
                break
    elif ops.lower() == 'anb':
        def ANB():
            typeanb = input("AnB ou AnBnC\nDesejá fazer qual das opiçoes a cima? ")
            if typeanb.lower() == 'anb':
                ops1 = int(input("Desejá quantos elementos? "))
                A = set()
                for i in range(ops1):
                    save1 = int(input("Digite o elemento: "))
                    A.add(save1)
                ops2 = int(input("Desejá quantos elementos? "))
                B = set()
                for i in range(ops2):
                    save2 = int(input("Digite o elemento: "))
                    B.add(save2)
                print(f"A= {A}\nB={B}\nAUB={A.intersection(B)}")
            elif typeanb.lower() == 'anbnc':
                ops1 = int(input("Desejá quantos elementos? "))
                A = set()
                for i in range(ops1):
                    save1 = int(input("Digite o elemento: "))
                    A.add(save1)
                ops2 = int(input("Desejá quantos elementos? "))
                B = set()
                for i in range(ops2):
                    save2 = int(input("Digite o elemento: "))
                    B.add(save2)
                ops3 = int(input("Desejá quantos elementos? "))
                C = set()
                for i in range(ops3):
                    save3 = int(input("Digite o elemento: "))
                    C.add(save3)
                print(f"A= {A}\nB={B}\nC={C}\nAUB={A.intersection(B and C)}")
        while True:
            ANB()
            restcont = input("Deseja realizar a conta novamente? ")
            if not restcont.lower() in ['sim','yes','1']:
                break
    elif ops.lower() == 'complemento':
        def comp():
            ops1 = int(input("Desejá quantos elementos? "))
            A = set()
            for i in range(ops1):
                save1 = int(input("Digite o elemento: "))
                A.add(save1)
            ops2 = int(input("Desejá quantos elementos? "))
            B = set()
            for i in range(ops2):
                save2 = int(input("Digite o elemento: "))
                B.add(save2)
            print(f"A= {A}\nB={B}\nAUB={(A - B)}")
while True:
    codereset()
    resetcode = input("Desejá fazer outra operação? ")
    Del = input("Desejá limpar as contas anteriores? ")
    if Del.lower() in ['sim','yes','1']:
        os.system('cls' if os.name == 'nt' else 'clear')
    if not resetcode.lower in ['sim','yes','1']:
        print("________\nCodigo finalizado!")
        break
