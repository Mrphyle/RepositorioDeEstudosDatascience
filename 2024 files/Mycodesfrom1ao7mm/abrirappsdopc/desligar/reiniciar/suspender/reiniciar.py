#Reiniciar
import os
tempo_em_segundos = 6 * 10
print(f"O computador irá reiniciar em {tempo_em_segundos} segundos.")
os.system(f"shutdown /s /t {tempo_em_segundos}")
