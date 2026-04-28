# 11. Soma de Colunas: Crie uma matriz 3 x 3 e gere uma lista (array) de 3
# elementos onde cada elemento é a soma de uma coluna da matriz.

import numpy as np
matriz = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
soma = sum(matriz)
print(soma)