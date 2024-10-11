nota1, nota2, nota3, nota4 = float(input("Digite a nota= ")), float(input("Digite a nota= ")), float(input("Digite a nota= ")), float(input("Digite a nota= "))
media1 = float(nota1) + float(nota2) + float(nota3) + float(nota4)
media2 = media1 / 4
if media2 >= 7:
    print('Aluno aprovado')
else:
    if media2 < 4:
        print('Aluno reprovado')
    else:
        if media2 > 4 and media2 < 7:
            print('Aluno em recuperação')