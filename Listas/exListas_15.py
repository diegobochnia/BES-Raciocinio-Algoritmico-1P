# 15. Escreva um programa que rotacione os elementos de uma lista para a direita em n posições (Exemplo: a lista [1, 2, 3, 4, 5] com n=2 vira [4, 5, 1, 2, 3]).

lista = [1, 2, 3, 4, 5]
n = 2

lista_rotacionada = lista[-n:] + lista[:-n]

print(lista_rotacionada)