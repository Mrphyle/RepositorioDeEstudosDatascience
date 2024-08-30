Login = input("Faça assim:(Exemplo:Diego Dia: 10/04/24)\n\nQual o nome e dia de emição do pedido? ")
Quantia = float(input("Qual a quantidade de placas que desejá? "))
Largurasign = float(input("Qual a largura da placa? "))
Alturasign = float(input("Qual a altura da placa? "))
Script = input("O que será escrito? ")
removespace = (Script.strip().replace(" "," "))
Corsign = input("Qual cor você desejá branco ou cinza? ")
print("___________________________")
CorScript = input("azul\nvermelho\namarelo\npreto\nverde\nQual das cores acima será escrito a frase? ")
def ValorTotal():
    Areasign = (Largurasign*Alturasign)
    CustoMaterial = Areasign * 147.30
    CustoDesenho = (len(removespace)* 0.37)
    ValorPlaca =(CustoMaterial+CustoDesenho)
    return ValorPlaca
Prazo = (Quantia/6)
total = ValorTotal() * Quantia
print(f"_______________________________\nCadastro: {Login}\nQuantidade: {Quantia}\ntamanho: {Alturasign} x {Largurasign}\nFrase: {Script}\nCor da placa: {Corsign}\nCor da letra: {CorScript}")
print(f"_______________________________\nArea:{Largurasign*Alturasign}M^2\nMaterial:R${(Largurasign*Alturasign) * 147.30}\nfrase:R${round(len(removespace)* 0.37)}\nValor total:R${total}\n_______________________________")