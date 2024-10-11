#https://mybrowseraddon.com/dark-mode.html
#pip install googletrans
#pip install googletrans==4.0.0-rc1
#pip install pyperclip
def repeatranslatorcode():
    from googletrans import Translator
    import pyperclip
    firstlanguage= input("type the phrase or word to translate: ")
    languagetotranlate= input("type the lenguage that you want to tranlate: ")
    def translator_language():
        if languagetotranlate.lower() == "english":
            def translate_eng():
                translator = Translator()
                translator.translate(firstlanguage)#ex:"Ola mundo"
                print(f"\noriginal language: {firstlanguage}\n")
                translated = translator.translate(firstlanguage, dest="en")
                print(f"translate to english: {translated.text}")
            translate_eng()
        elif languagetotranlate.lower() == "portuguese" or "ptbr":
            def translate_ptbr():
                translator = Translator()
                translator.translate(firstlanguage)#ex:"Ola mundo"
                print(f"\noriginal language: {firstlanguage}\n")
                translated = translator.translate(firstlanguage, dest="pt")
                print(f"translate to ptbr: {translated.text}")
                copi= input("you want copy this translation(y/n)? ")
                if copi.lower() ==  "y":
                    pyperclip.copy(translated.text)
                else:
                    pass
            translate_ptbr()
    translator_language()
while True:
    repeatranslatorcode()
    repeatcode = input("\n-------------\nyou want translate other phrase(y/n)? ")
    if repeatcode.lower() == "y":
        print("\n\n-------\n")
        pass
    elif repeatcode.lower() =="n":
        print("\n code finished!\n---------")
        break