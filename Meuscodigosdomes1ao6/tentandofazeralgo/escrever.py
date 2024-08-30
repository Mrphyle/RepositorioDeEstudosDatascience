import pyautogui
import time
escreva = input("O que desejá escrever? ")
time.sleep(5)
pyautogui.write(escreva, interval=0.05)