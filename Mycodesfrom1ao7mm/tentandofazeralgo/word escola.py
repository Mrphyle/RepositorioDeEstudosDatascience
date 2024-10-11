import time
import pyautogui as pyauto
pyauto.click(x=67, y=91)
time.sleep(1)
pyauto.click(x=101, y=255)
time.sleep(10)
pyauto.click(x=259, y=275)
time.sleep(10)
pyauto.write("""Toronto ontario canada fala de um jeito mais calmo, 
tem um pouco de chiado e parece puchar um pouquinhio o rem geral achei bem legivel

New York Usa eles falam mais rapido do que os canadences, 
mas não possui tanto chiado, e os euasparecem falar mais alto
united kingdon
Resumindo: Falam no modo 2x e não da para entendender quase nenhuma palavra
comparado com canada e estados unidos""",interval=0.1)