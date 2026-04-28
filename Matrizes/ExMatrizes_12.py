# 12.Verificação de Simetria: Verifique se uma matriz quadrada é simétrica (onde
# a matriz é igual à sua transposta).

import numpy as np

matriz = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

matriz_transposta = matriz.T

sao_iguais = np.array_equal(matriz, matriz_transposta)

print("As matrizes são simétricas? ", sao_iguais)
