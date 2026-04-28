# 6. Contagem de Pares: Dada uma matriz 3 x 4, conte quantos números pares
# ela possui.

import numpy as np

matriz3x4 = np.array((
    (22, 57, 11, 84),
    (39,  6, 73, 42),
    (95, 18, 50, 61)
))

cont = 0
for i in range(len(matriz3x4)):
    for j in range(len(matriz3x4[i])):
        if (matriz3x4[i][j]) % 2 == 0:
            cont += 1


print(matriz3x4)
print()
print(f"A matriz acima possui {cont} números pares.")