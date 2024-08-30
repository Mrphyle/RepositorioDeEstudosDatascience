import os
import time
import tkinter as tk
import pyautogui as pa
import pyperclip as pc
class Buttontype:
    @staticmethod
    def spotify_location():
        spotifile = r"C:\Users\hoolf\AppData\Roaming\Spotify\Spotify.exe"
        os.startfile(spotifile)
    @staticmethod
    def chrome_location():
        chromefile = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(chromefile)
        Fdmfile= r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Free Download Manager\Free Download Manager.lnk"
        os.startfile(Fdmfile)
    @staticmethod
    def Drive_location():
        drivefile = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Drive.lnk"
        os.startfile(drivefile)

    @staticmethod
    def Obs_location():
        obsfile = r"C:\Users\Public\Desktop\OBS Studio.lnk"
        os.startfile(obsfile)
    @staticmethod
    def Wallpaperengine_location():
        wallpaperenfile = r"C:\Users\hoolf\Desktop\Wallpaper Engine.url"
        os.startfile(wallpaperenfile)
    @staticmethod
    def Clippaint_location():
        clipstudiofile = r"C:\Program Files\CELSYS\CLIP STUDIO 1.5\CLIP STUDIO PAINT\CLIPStudioPaint.exe"
        os.startfile(clipstudiofile)
    @staticmethod
    def Huionh64_locate():
        huionhs64file = r"C:\Program Files\HuionTablet\HuionTablet.exe"
        os.startfile(huionhs64file)
    @staticmethod
    def steam_locate(): #lucasdamanga #123456
        steamfile= r"C:\Program Files (x86)\Steam\steam.exe"
        os.startfile(steamfile)
    @staticmethod
    def mine_location():
        minefile = r"C:\XboxGames\Minecraft Launcher\Content\Minecraft.exe"
        os.startfile(minefile)
    @staticmethod
    def teams_open():
        browser= r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        web="https://teams.microsoft.com/v2/"
        os.startfile(browser)
        time.sleep(5)
        pa.write(web)
        pa.hotkey("enter")
        pc.copy("goncalves1807")
    @staticmethod
    def taskmng_comand():
        pa.hotkey('ctrl','shift','esc')
    @staticmethod
    def sometimes_script():
        class Buttontype2:
            @staticmethod
            def webcam_file():
                webcam_location = r"C:\Program Files (x86)\DroidCam\DroidCamApp.exe"
                os.startfile(webcam_location)
            @staticmethod
            def xamp_file():
                xamp_location = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\XAMPP\XAMPP Control Panel.lnk"
                os.startfile(xamp_location)
            @staticmethod
            def Soudpad_file():
                Soudpad_location = r"C:\Users\hoolf\Downloads\Soundpad\Soundpad\Soundpad.exe"
                os.startfile(Soudpad_location)
        somentimesroot = tk.Tk()
        somentimesroot.geometry("800x600")
        somentimesroot.title("Abridor de aplicativos 2.0")
        somentimesroot.configure(bg='gray20')
        button_style = {
            'bg': 'gray30',
            'fg': 'white',
            'activebackground': 'gray50',
            'activeforeground': 'white',
            'height': 3,
            'width': 20
        }
        #Titulo
        title_text = tk.Text(somentimesroot, height=1, bg='gray20', fg='white', font=('Helvetica', 16), bd=0)
        title_text.pack(pady=20)
        title_text.insert(tk.END, "Clique no app que deseja abrir abaixo:")
        title_text.configure(state='disabled')
        #webcam
        webcam_button = tk.Button(somentimesroot,text="Webcam",command= Buttontype2.webcam_file,**button_style)
        webcam_button.place(x=20,y=1*75)
        #xamp
        xamp_button = tk.Button(somentimesroot,text="xamp",command= Buttontype2.xamp_file,**button_style)
        xamp_button.place(x=20,y=2*75)
        #SoundPad
        soudpad_button = tk.Button(somentimesroot,text="SoundPad",command=Buttontype2.Soudpad_file,**button_style)
        soudpad_button.place(x=20,y=3*75)
        somentimesroot.mainloop()
# Criar a janela principal
root = tk.Tk()
root.geometry("800x600")
root.title("Application Opener 2.0")
root.configure(bg='gray20')
button_style = {
    'bg': 'gray30',
    'fg': 'white',
    'activebackground': 'gray50',
    'activeforeground': 'white',
    'height': 3,
    'width': 20
}
#Titulo
title_text = tk.Text(root, height=1, bg='gray20', fg='white', font=('Helvetica', 16), bd=0)
title_text.pack(pady=20)
title_text.insert(tk.END, "Click on the app you want to open below:")
title_text.configure(state='disabled')
# Spotify
spotify_button = tk.Button(root, text="Spotify", command=Buttontype.spotify_location, **button_style)
spotify_button.place(x=20,y=1*75)
# Chrome
chrome_button = tk.Button(root, text="Google\nChrome", command=Buttontype.chrome_location, **button_style)
chrome_button.place(x=20,y=2*75)
#Drive
drive_button = tk.Button(root,text="Google\nDrive",command=Buttontype.Drive_location,**button_style)
drive_button.place(x=20,y=3*75)
#Obs_location
obs_button = tk.Button(root,text="OBS",command=Buttontype.Obs_location,**button_style)
obs_button.place(x=20,y=4*75)
#clipstudio
clipstudiopaint_button = tk.Button(root, text="ClipStudio\nPaint",command=Buttontype.Clippaint_location, **button_style)
clipstudiopaint_button.place(x=225,y=75)
#huionsoftuware
huionhs64_button = tk.Button(root,text="Huion hs64\nSoftware",command=Buttontype.Huionh64_locate,**button_style)
huionhs64_button.place(x=225,y=2*75)
#wallpaperengine
wallpprengbutton = tk.Button(root,text="wallpaper\nengine",command=Buttontype.Wallpaperengine_location,**button_style)
wallpprengbutton.place(x=225,y=3*75)
#steam
steam_button = tk.Button(root,text="Steam",command=Buttontype.steam_locate,**button_style)  
steam_button.place(x=225,y=4*75)
#taskmanager
taksmng_button = tk.Button(root,text="task manager",command=Buttontype.taskmng_comand,**button_style)
taksmng_button.place(x=430,y=2*75)
#teams
teams_button= tk.Button(root, text="Teams",command=Buttontype.teams_open,**button_style)
teams_button.place(x=430,y=3*75)
#minecraft
mine_button= tk.Button(root,text="Minecraft\nLauncher",command=Buttontype.mine_location,**button_style)
mine_button.place(x=430,y=4*75)
#apps que uso de vez em nunca
sometimes_button = tk.Button(root,text="sometimes",command=Buttontype.sometimes_script,**button_style)
sometimes_button.place(x=430,y=1*75)
root.mainloop()