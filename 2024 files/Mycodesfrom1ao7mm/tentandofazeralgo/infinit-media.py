"""def arr(numbers):
    liste= []
    for i in range(liste):
        media=+ liste[i]
    for i in range(numbers):
        NumbersToCount = int(input("digite o numero que deseja: "))
        liste.append(NumbersToCount)
    rusult_media = media/numbers
    return rusult_media

number_count = int(input("quantos numeros você fara a media? "))
media = arr(number_count)"""
def arr(numbers):
    liste = []
    media = 0  # Inicializa a media como 0
    for i in range(numbers):  # Loop para obter os números
        NumbersToCount = int(input("digite o numero que deseja: "))
        print("\n")
        liste.append(NumbersToCount)
    
    for i in range(numbers):  # Loop para somar os números
        media += liste[i]  # Soma os números da lista

    rusult_media = media / numbers
    print(f"{media}/{numbers}")  # Cálculo da média
    return rusult_media

number_count = int(input("quantos numeros você fara a media? "))
media = arr(number_count)
print("A média é:", media)