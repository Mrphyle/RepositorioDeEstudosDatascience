def restartaula():
    AulasCD1 = input("Inicio do registro22/03\nex:Aula1\nQual aula deseja? ")
    if AulasCD1.lower() == 'aula1':
        # auladia2203ex1.py
        nt = int(input("Type tabuada: "))
        it = range(1, 11)
        for t in it:
            print(f"{t} X {nt} = {nt * t}")
    elif AulasCD1.lower() == 'aula2':
        esanble = {'Ana', 'Julia', 'Eduarda', 'Maria'}
        for name in esanble:
            print(name)
        NewName = input("New name: ")
        esanble.add(NewName)
        for name in esanble:
            print(name)

while True:
    restartaula()
    resaula = input("Deseja executar outra aula? (Sim/Não): ")
    if resaula.lower() != "sim":
        break