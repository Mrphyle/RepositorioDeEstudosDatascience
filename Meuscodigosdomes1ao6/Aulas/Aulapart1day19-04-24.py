def ResetCode():
    while True:
        ops = input("Digite 1 , 2 ou 3: ")
        if ops == '1':
            # imprime uma lista com os números primos
            n1 = int(input("Digite o número que vai começar? "))
            n2 = int(input("Digite o número máximo que irá separar de ímpar do par: "))
            if n1 % 2 == 0:
                n1 = n1 + 1
            i = list(range(n1, n2 + 1, 2))
            print(i)
        elif ops == '2':
            Tipolista = input("\n____________________\nTupla\nConjunto\nQual lista acima deseja? ")
            if Tipolista.lower() == 'tupla':
                tupla = (10, 24, 34)
                print(tupla)
            elif Tipolista.lower() == 'lista':
                Lista = ['Eliandro', 24, 267]
                Lista.extend()
                print(Lista)
            elif Tipolista.lower() == 'conjunto':
                c = {0, 1, 2, 3, 4, 5, 6, 7}
                nomes = {'Ana', 'Diego', 'nina'}
                print(f"{c}\n{nomes}")
            elif Tipolista.lower() == 'dicionario':
                pessoa = {'nome': 'Diego Simão Gonçalves', 'Idade': 16}
                print(pessoa)
                pessoa.update({'DateNasc': '07/12/2007'})
                print(f"\n{pessoa}")
                pessoa.update({'cargo': 'Cientista de dados'})
        resetcode = input("_______________\n\nQuer reiniciar o código? ")
        if resetcode.lower() != 'sim' and resetcode.lower() != 'yes':
            print('_____________\nCódigo Finalizado!')
            break
ResetCode()