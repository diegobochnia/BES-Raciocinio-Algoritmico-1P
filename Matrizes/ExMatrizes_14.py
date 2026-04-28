# 14.Multiplicação de Matrizes: Implemente a multiplicação de duas matrizes.
# Lembre-se: para multiplicar A por B, o número de colunas de A deve ser igual
# ao número de linhas de B.

import numpy as np

a = np.array([
    [2, 3, 4],
    [2, 3, 4]
])

b = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
mult = np.dot(a, b)

print(a)
print()
print(b)
print()
print("A multiplicação entre as duas matrizes resulta em: \n", mult)