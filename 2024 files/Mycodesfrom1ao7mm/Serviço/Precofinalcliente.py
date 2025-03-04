#Enter1
opdeservico = input("(Obs: Escreva 'Album fotografico' ou 'Encadernação' ou 'Caixa' ou 'Impressão' ou 'Pendrive' ou 'Baner')\n Qual produto você deseja? ")
if opdeservico == 'Album fotografico':
    #Enter2
    TipoAlbum= input("(Escreva: 'couro' ou 'acrilico' ou 'madeira' ou 'tecido' ou 'capafotografica')\nQual o tipo do album? ")
    if TipoAlbum == 'Couro':
        #Enter
        TipoCouro= input("(Escreva: 'Gravado' ou 'Janela' ou 'Bordado')\nQual o tipo do Couro? ")
        #Process
        if TipoCouro == 'Gravado':
            ValCapa= float(input("Qual o valor da capa? "))
            QuantLami = float(input("Qual a quantidade de laminas que será feita? "))
            ValLamiUni = float(input("Qual o valor da unidade da lamina? "))
            Work= float(input("Qual o valor do trabalho feito?"))
            Result = (QuantLami * ValLamiUni) + ValCapa + Work
            #Exit
            print("Preço do Album sairá R$",Result)
        elif TipoCouro == 'Janela':
            ValCapa= float(input("Qual o valor da capa? "))
            QuantLami = float(input("Qual a quantidade de laminas que será feita? "))
            ValLamiUni = float(input("Qual o valor da unidade da lamina? "))
            Work= float(input("Qual o valor do trabalho feito?"))
            Result = (QuantLami * ValLamiUni) + ValCapa + Work
            #Exit
            print("Preço do Album sairá R$",Result)
        elif TipoCouro == 'Bordado':
            ValCapa= float(input("Qual o valor da capa? "))
            QuantLami = float(input("Qual a quantidade de laminas que será feita? "))
            ValLamiUni = float(input("Qual o valor da unidade da lamina? "))
            Work= float(input("Qual o valor do trabalho feito?"))
            Result = (QuantLami * ValLamiUni) + ValCapa + Work
            #Exit
            print("Preço do Album sairá R$",Result)
    elif TipoAlbum == 'acrilico':
        #Enter
        
        #Process
        
        #Exit
        print("Preço do Album sairá R$",)
    elif TipoAlbum == 'madeira':
        #Enter
        TipoMadeira = input("Escreva:('janela' ou 'acrilico')\nQual o tipo de album de madeira? ")
        #Process
        if TipoMadeira == 'janela':
        elif TipoAlbum == 'tecido':
        #Enter
        
        #Process
        
        #Exit
        print("Preço do Album sairá R$")
    elif TipoAlbum == 'capafotografica':
        #Enter

        #Process
        
        #Exit
        print("Preço do Album sairá R$",)
    elif TipoAlbum == '':
        #Enter

        #Process
        
        #Exit
        print("Preço do Album sairá R$",)
elif opdeservico == 'Encadernação':
    #Enter
    TipoEncadernacao = input("(Escreva: 'airo' ou 'espiral' ou 'capadura')\nQual o tipo da encadernação? ")
        #Process
    if TipoEncadernacao == 'airo':
        ValAiro= float(input("Qual o tipo de quantidade de folhas?"))
        if ValAiro <= 100:
            print("Preço do airo sairá R$15,00")
        if ValAiro > 100 and ValAiro <= 150:
            print("Preço do airo sairá R$20,00")
        if ValAiro > 100 and ValAiro > 150 and ValAiro <= 250:
            print("Preço do airo sairá R$25,00")
    elif TipoEncadernacao == 'Restauração':
        #Enter

        #Process
        
        #Exit
        print("A restauração sairá R$",)
elif opdeservico == 'Caixa':
    TipoCaixa = input("(Escreva: 'Maleta' ou 'Luva' ou '')\nQual o tipo da Caixa? ")
    if TipoCaixa == 'Maleta':
        #Enter

        #Process
        
        #Exit
        print("Preço da maleta sairá R$",)
    elif TipoCaixa == 'Luva':
        #Enter

        #Process
        
        #Exit
        print("Preço da luva sairá R$",)
elif opdeservico == 'Impressão':
    TipoPrint = input("(Escreva: 'Fotografico' ou 'Sulfite' ou '')\nQual o tipo da Caixa? ")
    if TipoPrint == 'Fotografico':
        #Enter

        #Process
        
        #Exit
        print("Preço da impreção em Papel fotografico sairá R$",)
    elif TipoPrint == 'Sulfite':
        #Enter

        #Process
        
        #Exit
        print("Preço da impreção em Papel Sulfite sairá R$",)
elif opdeservico == 'Pendrive':
    TipoPendrive = input("(Escreva: 'Maleta' ou 'Luva' ou '')\nQual o tipo da Caixa? ")
    if TipoPendrive == 'Maleta':
        #Enter

        #Process
        
        #Exit
        print("Preço da maleta sairá R$",)
    elif TipoPendrive == 'Luva':
        #Enter

        #Process
        
        #Exit
        print("Preço da luva sairá R$",)
elif opdeservico == 'Baner':
    TipoBaner = input("(Escreva: '' ou 'Luva' ou '')\nQual o tipo da Caixa? ")
    if TipoBaner == 'Maleta':
        #Enter

        #Process
        
        #Exit
        print("Preço da maleta sairá R$",)
    elif TipoBaner == 'Luva':
        #Enter

        #Process
        
        #Exit
        print("Preço da luva sairá R$",)