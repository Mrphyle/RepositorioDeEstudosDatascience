import pyautogui
import pyperclip
import threading
import time
import os
import pygame
Ctrlvortimerset = input("Timer\nCrtl + V\nTimer ou ctrlV? ")
def png():
    file_directory = r"C:\Users\hoolf\Downloads\python (3)\Codigos test"
    soundalert = os.path.join(file_directory, "alarm.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load(soundalert)
    pygame.mixer.music.play(loops=-1)
    while True:
        time.sleep(1)
if Ctrlvortimerset.lower() == 'ctrlv' or Ctrlvortimerset.lower() == 'ctrl v':
    def alttab():
        pyautogui.hotkey('alt','tab')
        time.sleep(2)
        pyautogui.click
    alttab()
    def pyautoguiexecuter():
        vezes = 10
        contador = 0 
        while contador < vezes:
            pyperclip.copy('$wa')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            contador += 1
            time.sleep(1)
    TIMe = 5
    Recressive_time = threading.Thread(target=pyautoguiexecuter)
    Recressive_time.start()
    for i in range(TIMe, 0, -1):
        print(i)
        time.sleep(1)
    Recressive_time.join()
elif Ctrlvortimerset.lower() == 'timer':
    def Executertimercode(Time):
        for i in range(Time, -1, -1):
            minutos = i // 60
            segundos = i % 60
            print(f"                                                                  {minutos:02}:{segundos:02}", end='\r')
            time.sleep(1)
    timerset = int(input("Quantos minutos vocÃª quer? "))
    timersec = timerset * 60
    TIMe = timersec
    Recressivetime = threading.Thread(target=Executertimercode, args=(TIMe,))
    Recressivetime.start()
    Recressivetime.join()
    png()
    