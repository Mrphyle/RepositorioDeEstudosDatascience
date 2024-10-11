def Resetcode():
    ops = input("Digite As opições 1 ou 2: ")
    if ops == '1':
        Placa = []
        Placa.append("Placa"),Placa.append(170),Placa.append(184),Placa.append("18/04/24")
        print(Placa)
    elif ops == '2':
        Altura = []
        SomAlt = 0
        MaiorAlt = 0
        MenorAlt = 500
        for i in range(4):
            Altura.append(int(input("Digite a Altura: ")))
            SomAlt+=Altura[i]
            if MaiorAlt<Altura[i]:
                MaiorAlt=Altura[i]
            if MenorAlt>Altura[i]:
                MenorAlt=Altura[i]        
        print(f"Lista: {Altura}\nA média é {SomAlt/4}\nMaior altura = {MaiorAlt}\nMenor altura = {MenorAlt}\n\n_________________________")
while True:
    Resetcode()
    ResetCode = input("Quer recomeçar o codigo? ")
    if ResetCode.lower() in['no','não','0']:
        break