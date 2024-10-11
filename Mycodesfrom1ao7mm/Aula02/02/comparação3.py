saldo,saque = float(input('quanto é seu saldo?= ')),float(input('quanto quer sacar?= '))
if saldo >= saque:
    resto = saldo - saque
    print('Pode retirar o dinheiro você tem é o sulficiente','sobrou R$',resto,'em sua conta')
else:
    print('Seu saldo não é o sulficiente')   