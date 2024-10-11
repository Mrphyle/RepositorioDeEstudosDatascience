def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # Flag para detectar se houve troca na iteração
        trocado = False
        for i in range(0, n - i - 1):
            if lista[i] > lista[i + 1]:
                # Troca de elementos
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocado = True
        # Se não houve trocas, a lista já está ordenada
        if not trocado:
            break
    return lista

# Exemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(lista))
