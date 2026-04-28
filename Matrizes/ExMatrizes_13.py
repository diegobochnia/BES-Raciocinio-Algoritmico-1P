# 13.Diagonal Secundária: Exiba apenas os elementos da diagonal secundária
# de uma matriz 5 x 5.

import numpy as np

matriz = np.array((
    (12, 85, 43, 21, 67),
    (34,  9, 91, 55, 18),
    (76, 42,  5, 88, 30),
    (29, 63, 14, 72, 49),
    (51, 97, 38,  6, 84)
))

diagonal_secundaria = np.diag(np.fliplr(matriz))

print("Os elementos da diagonal secundária são: ", diagonal_secundaria)