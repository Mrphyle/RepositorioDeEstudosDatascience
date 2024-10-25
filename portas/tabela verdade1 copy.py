escolha_porta = input("qual das  portas abaixo  deseja ver?\nand\nor\nxor\nnand\nnor\nxnor ")
def porta_and():
    while True:
        a = input("Se A for 1 ou 0 digite este numero: ")
        b= input("Ser B for 1 ou 0 digite este numero: ")
        a1= True
        a0 = False
        b1 = True
        b0 = False
        if a == "0" and b == "0":
            print(a0 and b0,"=0") 

        if a == "0" and b == "1":
            print(a0 and b1,"=0")

        if a == "1" and b == "0":
            print(a1 and b0,"=0")

        if a == "1" and b == "1":
            print(a1 and b1,"=1")
def porta_or():
    while True:
        a = input("Se A for 1 ou 0 digite este numero: ")
        b= input("Ser B for 1 ou 0 digite este numero: ")
        a1= True
        a0 = False
        b1 = True
        b0 = False
        if a == "0" and b == "0":
            print(a0 or b0,"=0") 

        if a == "0" and b == "1":
            print(a0 or b1,"=1")

        if a == "1" and b == "0":
            print(a1 or b0,"=1")

        if a == "1" and b == "1":
            print(a1 or b1,"=1")
def porta_xor():
    while True:
        a = input("Se A for 1 ou 0 digite este numero: ")
        b= input("Ser B for 1 ou 0 digite este numero: ")
        a1= True
        a0 = False
        b1 = True
        b0 = False
        if a == "0" and b == "0":
            print(a0 ^ b0,"=0") 

        if a == "0" and b == "1":
            print(a0 ^ b1,"=1")

        if a == "1" and b == "0":
            print(a1 ^ b0,"=1")

        if a == "1" and b == "1":
            print(a1 ^ b1,"=0")
def porta_nand():
    while True:
        a = input("Se A for 1 ou 0, digite este número: ")
        b = input("Se B for 1 ou 0, digite este número: ")
        a1 = True
        a0 = False
        b1 = True
        b0 = False

        if a == "0" and b == "0":
            print(not (a0 and b0), "=1")

        if a == "0" and b == "1":
            print(not (a0 and b1), "=1")

        if a == "1" and b == "0":
            print(not (a1 and b0), "=1")

        if a == "1" and b == "1":
            print(not (a1 and b1), "=0")
def porta_nor():
    while True:
        a = input("Se A for 1 ou 0, digite este número: ")
        b = input("Se B for 1 ou 0, digite este número: ")
        a1 = True
        a0 = False
        b1 = True
        b0 = False

        if a == "0" and b == "0":
            print(not (a0 or b0), "=1")

        if a == "0" and b == "1":
            print(not (a0 or b1), "=0")

        if a == "1" and b == "0":
            print(not (a1 or b0), "=0")

        if a == "1" and b == "1":
            print(not (a1 or b1), "=0")

def porta_xnor():
    while True:
        a = input("Se A for 1 ou 0, digite este número: ")
        b = input("Se B for 1 ou 0, digite este número: ")
        a1 = True
        a0 = False
        b1 = True
        b0 = False

        if a == "0" and b == "0":
            print(not (a0 ^ b0), "=1")

        if a == "0" and b == "1":
            print(not (a0 ^ b1), "=0")

        if a == "1" and b == "0":
            print(not (a1 ^ b0), "=0")

        if a == "1" and b == "1":
            print(not (a1 ^ b1), "=1")
def fescolha_porta():
    if escolha_porta.lower() == "and":
        porta_and()
    elif escolha_porta.lower() == "or":
        porta_or()
    elif escolha_porta.lower() == "xor":
        porta_xor()
    elif escolha_porta.lower() == "nand":
        porta_nand()
    elif escolha_porta.lower() == "nor":
        porta_nor()
    elif escolha_porta.lower() == "xnor":
        porta_xnor()
fescolha_porta()