def porta_xor():
    while True:
        a = input("Se A for 1 ou 0 digite este numero: ")
        b= input("Ser B for 1 ou 0 digite este numero: ")
        a1= True
        a0 = False
        b1 = True
        b0 = False
        if a == "0" and b == "0":
            print(a0 ^ b0,"0") 

        if a == "0" and b == "1":
            print(a0 ^ b1,"1")

        if a == "1" and b == "0":
            print(a1 ^ b0,"1")

        if a == "1" and b == "1":
            print(a1 ^ b1,"0")
porta_xor()