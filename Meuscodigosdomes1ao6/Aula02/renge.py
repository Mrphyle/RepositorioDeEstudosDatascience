Range = input("Range 1 or range 2 digite ou 'Range1' ou 'range2'= ")
if Range == 'Range1':
    tabuada = float(input("Digite o numero da tabuada= "))
    for i in range(1,11):
        print(i,'*',tabuada,'=',i * tabuada)
elif Range == 'range2':
    for i in range(1,11):
        for w in range(1,11):
            print(i,'*',w,"=",w * i)