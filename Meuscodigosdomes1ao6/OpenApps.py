import os
import time
import webbrowser
import pyperclip as pc
import pyautogui as pa
def whatsappopen():
    pc.copy("https://chat.openai.com/")
    os.system('cls' if os.name == 'nt' else 'clear')
    WhatsAppOpen = input("_________________________________\nBrowsers(List of browsers)\nBrowser P(Default)\nSpotify\nDeepl\nOpen a website\nSpeedtest\nAudacity\nWhich of the above do you want to start? ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if WhatsAppOpen.lower() == 'browsers':
        def navigations():
            os.system('cls' if os.name == 'nt' else 'clear')
            BrowserOptions = input("Google\nOperaGX\nEdge\nWhich of the available browsers above do you want? ")
            if BrowserOptions.lower() == 'google' :
                os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
                print("\nOpening Google Chrome....")
            elif BrowserOptions.lower() in ['opera gx', 'operagx']:
                os.startfile(r"C:\Users\hoolf\AppData\Local\Programs\Opera GX\launcher.exe")
                print("\nOpening Opera Gx....")
        while True:
            navigations()
            restartcont = input("\nDo you want to open another browser? ")
            if not restartcont.lower() in ['yes', 'no', '1']:
                print("________________________\n")
                break
    if WhatsAppOpen.lower() == 'browser p':
        os.startfile(r"C:\Users\hoolf\AppData\Local\Programs\Opera GX\launcher.exe")
        print("\nOpening Opera Gx....")
    if WhatsAppOpen.lower() == 'spotify':
        os.startfile(r"C:\Users\hoolf\AppData\Roaming\Spotify\Spotify.exe")
        print("\nOpening Spotify....")
    if WhatsAppOpen.lower() == 'deepl':
        os.startfile(r"C:\Users\hoolf\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\DeepL")
        print("\nOpening DeepL....")
    if WhatsAppOpen.lower() == 'speedtest':
        os.startfile(r"C:\Program Files\Speedtest\Speedtest.exe")
        print("\nOpening Speedtest")
    if WhatsAppOpen.lower() == 'open site':
        websites = input("\nRadio Garden\nEnter one of these sites above or type a URL: ")
        if websites.lower() == 'radio garden':
            web = "https://radio.garden/listen/country-101-1/B34md32h"
            webbrowser.open(web)
            print(f"\nOpening the site: {websites}")
        elif websites.lower() == 'teams':
            pc.copy("goncalves1807")
            web = "teams.microsoft.com/v2/#/school/teams-grid/General?ctx=teamsGrid"
            pa.hotkey('alt', 'tab')
            time.sleep(1)
            pa.hotkey('ctrl', 't')
            time.sleep(2)
            pa.write(web)
            pa.hotkey('enter')
            time.sleep(30)
            pa.click(x=1861, y=137)
            time.sleep(10)
            pa.click(x=1128, y=553)
            time.sleep(30)
            pa.click(x=70, y=350)
            print(f"\nOpening the site: {websites}")
        else:
            webbrowser.open(websites)
    if WhatsAppOpen.lower() == 'audacity':
        os.startfile(r"C:\Program Files\Audacity\Audacity.exe")
        print("\nOpening Audacity....")
while True:
    whatsappopen()
    restartcont = input("\nDo you want to open another application? ")
    if restartcont.lower() in ['yes', 'y', '1']:
        continue
    else:
        print('___________________\nCommand completed')
        break       