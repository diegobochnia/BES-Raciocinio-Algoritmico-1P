# 20.Escreva uma função recursiva que receba uma lista de números distintos e
# retorne todas as permutações possíveis de seus elementos.

def permutar(lista):
    if len(lista) <= 1:
        return [lista]

    resultado = []

    for i in range(len(lista)):
        fixo = lista[i]
        sobra = lista[:i] + lista[i + 1:]

        for p in permutar(sobra):
            resultado.append([fixo] + p)

    return resultado


minha_lista = [-2, 1, -3, 4]
todas_as_permutacoes = permutar(minha_lista)

print(f"Lista original: {minha_lista}")
print()

print(f"Todas as permutações possíveis: ")
for item in todas_as_permutacoes:
    print(item)

