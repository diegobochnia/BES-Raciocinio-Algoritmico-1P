# 19. Dada uma lista de números inteiros (positivos e negativos), encontre a
# sublista contígua com a maior soma e retorne o valor dessa soma (Algoritmo
# de Kadane).


def kadane(lista):
    atual = lista[0]
    maximo = lista[0]


    for item in lista[1:]:
        atual = max(item, atual + item)
        maximo = max(atual, maximo)
    return maximo

minha_lista = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
resultado = kadane(minha_lista)
print(f"A maior soma encontrada foi: {resultado}")

