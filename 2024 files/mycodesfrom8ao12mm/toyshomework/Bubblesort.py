while True:
    List = []
    inputnumberlist = int(input("when numbers you want add in this List? "))
    for i in range(inputnumberlist):
        inputnumbers_in_list = int(input("add number: "))
        List.append(inputnumbers_in_list)

    def bubblesort():
        nun = len(List)
        ligado = True
        while ligado:
            ligado = False
            for i in range(nun - 1):
                if List[i] > List[i + 1]:
                    temp = List[i]
                    List[i] = List[i + 1]
                    List[i + 1] = temp
                    ligado = True
            nun = nun - 1
    bubblesort()
    print(List,"\n")
    restartcode= input("you want restart this code? ")
    if restartcode.lower() == "y":
        pass
    else:
        break