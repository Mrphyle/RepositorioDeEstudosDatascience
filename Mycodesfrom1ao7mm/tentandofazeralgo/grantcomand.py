"""def arr(numbes):
    for i in range(numbes):
        NumbersToCount = int(input("digite o numero que deseja: "))       
number_count = int(input("quantos numeros você fara a media? "))
media = arr(number_count)"""
import pyautogui as pyauto
import time
pyauto.hotkey("ctrl","alt","t")
time.sleep(5)
pyauto.write("cd /opt/lampp/bin")
time.sleep(1.5)
pyauto.hotkey("enter")
time.sleep(1.5)
pyauto.write(" ./mysql -u root -p")
time.sleep(1)
pyauto.hotkey("enter")
time.sleep(0.7)
pyauto.hotkey("enter")