#imports nessesarios
import os
import pyautogui as pyauto
import time
import pandas as pd
#abrir sistema
app,web = (r"C:\Program Files\Google\Chrome\Application\chrome.exe"),(r"https://dlp.hashtagtreinamentos.com/python/intensivao/login")
os.startfile(app)
time.sleep(10)
pyauto.write(web)
pyauto.press("enter")
time.sleep(3)
#falezer login
pyauto.click(x=1264, y=382),pyauto.write("diegosimaogoncalves18@gmail.com")
pyauto.press("tab")
pyauto.write("goncalvos"),pyauto.press("tab")
pyauto.press("enter"),time.sleep(2)
#inportar base de dados do produto
file = r"C:\Users\hoolf\Desktop\sinchouse\sincpyhouse\Python power up\produtos.csv"
tabels = pd.read_csv(file)
#cadastração de produto
for i in tabels.index:
    code = str(tabels.loc[i,"codigo"])
    pyauto.click(x=1345, y=281)
    pyauto.write(code)
    pyauto.press("tab")
    #marca
    ma = str(tabels.loc[i,"marca"])
    pyauto.write(ma)
    pyauto.press("tab")
    #tipo
    Type =str(tabels.loc[i,"tipo"])
    pyauto.write(Type)
    pyauto.press("tab")
    #categoria
    Cat =str(tabels.loc[i,"categoria"])
    pyauto.write(Cat)
    pyauto.press("tab")
    #preço
    pu =str(tabels.loc[i,"preco_unitario"])
    pyauto.write(pu)
    pyauto.press("tab")
    #custo
    cu = str(tabels.loc[i,"custo"])
    pyauto.write(cu)
    pyauto.press("tab")
    #obs
    obs = str(tabels.loc[i,"obs"])
    if obs != "nan":
        pyauto.write("obs")
    pyauto.press("tab")
    pyauto.press("enter")
    time.sleep(1)
    pyauto.press("home")
    time.sleep(0.25)