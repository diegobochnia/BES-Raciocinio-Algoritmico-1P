# 8. Média por Linha: Crie uma matriz 3 x 3 e exiba a média aritmética dos
# valores de cada linha separadamente.

import numpy as np
matriz = np.array((
    (47, 12, 89),
    (31, 75,  4),
    (66, 22, 58)
))

media = np.mean(matriz, axis=1)
print(media)