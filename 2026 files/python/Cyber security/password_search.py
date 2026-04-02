caracteres = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
'''
novasenha = None
for i in range(62):
    for j in range(62):
        for k in range(62):
            for l in range(62):
                for m in range(62):
                    for n in range(62):
                        for o in range(62):
                            for p in range(62):
                                novasenha = str(caracteres[i]) + str(caracteres[j]) + str(caracteres[k]) + str(caracteres[l]) + str(caracteres[m]) + str(caracteres[n]) + str(caracteres[o]) + str(caracteres[p])
                                print(novasenha)'''

novasenha = None
for i in range(62):
    for j in range(62):
        for k in range(62):
            for l in range(62):
                for m in range(62):
                    for n in range(62):
                        for o in range(62):
                            for p in range(62):
                                for q in range(62):
                                    for r in range(62):
                                        for s in range(62):
                                            for u in range(62):
                                                for t in range(62):
                                                    novasenha = str(caracteres[i]) + str(caracteres[j]) + str(caracteres[k]) + str(caracteres[l]) + str(caracteres[m]) + str(caracteres[n]) + str(caracteres[o]) + str(caracteres[p]) + str(caracteres[q]) + str(caracteres[r]) + str(caracteres[s]) + str(caracteres[u])
                                                    print(novasenha)