def ConvertTemp():
    Fah = float(input("type number in Fah "))
    resultinC = (5/9) * (Fah - 32)
    RoundresultinC = round(resultinC)
    print(RoundresultinC)
while True:
    ConvertTemp()
    restartcont = input("Do another calculation? ")
    if restartcont.lower() == 'Yes':
        break