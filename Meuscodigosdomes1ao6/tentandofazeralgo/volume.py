def reset():
    volMenosMais = input("aumentar volume press '1'\nabaixar press '0': ")
    if volMenosMais == '1':
        import pyautogui

        def diminuir_volume(quantidade):
            for _ in range(quantidade):
                pyautogui.press('volumeup')

        # Solicitar ao usuário a quantidade de vezes que deseja diminuir o volume
        quantidade = int(input("Quer almentar quanto?"))

        # Chamar a função para diminuir o volume
        diminuir_volume(quantidade)
    else:
        import pyautogui

        def diminuir_volume(quantidade):
            for _ in range(quantidade):
                pyautogui.press('volumedown')

        # Solicitar ao usuário a quantidade de vezes que deseja diminuir o volume
        quantidade = int(input("Quer diminuir quanto? "))

        # Chamar a função para diminuir o volume
        diminuir_volume(quantidade)
while True:
    reset()
    resetcode = input("fazer denovo press('1'/sim) ou ('0'/não): ")
    if resetcode.lower() != '1':
        break
    print('Codigo resetado')
    print("_________________________")