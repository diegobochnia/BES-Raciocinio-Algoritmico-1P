# 1. Soma Total: Crie uma matriz 3 x 3 de números inteiros e exiba a soma de
# todos os elementos.
import numpy as np

matriz3x3 = np.array((
    (47, 14, 89),
    (37, 75,  4),
    (66, 22, 98)
))

soma = np.sum(matriz3x3)
print("A soma de todos os elementos da matriz é: ", soma)