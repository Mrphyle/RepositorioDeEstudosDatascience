#Enter
porcent = float(input("Digite a porcentagem (Obs:coloque 0. antes da porcentagem ex:0.45 = 45%) "))
Nporcent = float(input("Digite o numero "))
#process
import math
resultporcent = Nporcent * porcent
#Exit
if math.isclose(resultporcent, int(resultporcent)):
    print("A porcentagem de",Nporcent,"=",f"{int(resultporcent)}","%")
    input("Digite esc para finalizar ")
else:
    print("A porcentagem de",Nporcent,"=", f"{resultporcent:.2f}","%")
    input("Digite esc para finalizar ")