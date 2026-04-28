# 9. Soma da Diagonal Principal: Calcule a soma de todos os elementos que
# compõem a diagonal principal de uma matriz 4 x 4.

import numpy as np

matriz = np.array([
    [22, 57, 11, 84],
    [39,  6, 73, 42],
    [95, 18, 50, 61],
    [39,  6, 73, 42]
])

diagonal = np.diag(matriz)
soma = np.sum(diagonal)

print(matriz)
print()
print("A soma dos elementos da diagonal da matriz acime é: ", soma)
