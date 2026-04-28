# 14. Dada uma lista mista de números, crie uma nova lista contendo apenas os números ímpares da lista original.

lista_numeros = [566, 25, 398, 696, 335, 543, 46, 921, 979, 788, 18, 328, 431, 786, 76]
numeros_impares = []

for numero in lista_numeros:
    if numero % 2 != 0:
        numeros_impares.append(numero)

print(numeros_impares)