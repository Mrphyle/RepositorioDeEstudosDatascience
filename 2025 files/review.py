import matplotlib.pyplot as plt
while True:
    selected_option = int(input("\n---------------------------\nOpitions Select\nReviw Matplotlib[0]\nInterval like For in[1]\nInterval like While[2]\nExit[Press Enter]\n---------------------------\n"))
    def matplotib_reviw():
        categories = ['A', 'B', 'C', 'D']
        values = [15, 30, 45, 10]
        plt.bar(x=categories, height=values)
        plt.show()

    def interval_For_In():
        nota01 = int(input("Digite a nota 01: "))
        for i in range(nota01):
            print(i)
    def interval_While():
        nota01 = int(input("Digite a nota 01: "))
        i = 0
        while(nota01>=i):
            print(i)
            i = i+1
    def Alfabets_Letters():
        List = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        ABC=len(List)
        print(f"{ABC}" )
    def Difference_Names_Count():

        List_Names=["Jonh","Mary","Jonata","Mary","Jonh","Jonata","Mary","Senna","Ayrton"]
        distinct_names = set(List_Names)
        for i in distinct_names:
            print(f"{i} = {List_Names.count(i)}")
    if selected_option == 0:
        matplotib_reviw()
    elif selected_option == 1:
        interval_For_In()
    elif selected_option == 2:
        interval_While()
    elif selected_option == 3:
        Alfabets_Letters()
    elif selected_option == 4:
        Difference_Names_Count()
    else:
        print("Exiting...")