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
porta_nand()