import pyautogui
import time
pesquisar = input("O que desejá pesquisar? ")
pyautogui.hotkey("alt","tab")
pyautogui.hotkey("ctrl","t")
time.sleep(1)
pyautogui.write(pesquisar, interval=0.05)
pyautogui.press("enter")