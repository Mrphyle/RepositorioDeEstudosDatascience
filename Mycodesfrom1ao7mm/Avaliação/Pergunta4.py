idade = int(input("Digite a idade da pessoa: "))
classe_eleitoral = "Não votante"  # Default class
if idade >= 16:
  if idade <= 18 or idade > 65:
    classe_eleitoral = "Eleitor facultativo"
  else:
    classe_eleitoral = "Eleitor obrigatório"
print("Classe eleitoral:", classe_eleitoral)