#Possible paths to computer shutdown
input1= input("Digite 1 para desligamento instantaneo\nCaso queira definir um timer em segundos digite 2, se querer em minutos digite 3 ")
#Process1
if input1 == '1':
    import os
    tempo_em_segundos = 6 * 10
    print(f"O computador irá desligar em {tempo_em_segundos} segundos.")
    os.system(f"shutdown /s /t {tempo_em_segundos}")
#Process2
elif input1 == '2':
    import os
    tempo_em_segundos = float(input("Quantos segundos deseja? "))
    print(f"O computador irá desligar em {tempo_em_segundos} segundos.")
    os.system(f"shutdown /s /t {tempo_em_segundos}")
#Process3
    import os
    TempMn = float(input("Em quantos minutos deseja desligar? "))
    TempSecond = TempMn * 60
    print(f"O computador irá desligar em {TempMn} Minutos.")
    os.system(f"shutdown /s /t {TempSecond}")