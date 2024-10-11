precoetiq = float(input("Digite o preço "))
Condpgto =  input(" 'A vista' ou 'Cartão Crédito' e '2x cc' '3x cc' ")
if Condpgto == 'A vista':
    precopagar=precoetiq - precoetiq*0.1
if Condpgto == 'Cartão Crédito':
 precopagar = precoetiq - precoetiq*0.05
if Condpgto == '2x cc':
   precopagar = precoetiq - precoetiq*0.1
if Condpgto == '3x cc':
    precopagar = precoetiq + precoetiq*0.1
print('O preço a pagar é', precopagar)
input("Digite esc para finalizar ")