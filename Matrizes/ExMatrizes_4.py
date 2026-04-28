# 4. Troca de Valores: Crie uma matriz 2 x 2 e troque os valores da primeira linha
# com os da segunda linha.

import numpy as np

matriz2x2 = np.array((
    (14, 55),
    (92, 37)
))
print("Matriz original:\n", matriz2x2)
matriz_nova = matriz2x2[::-1]
print("-" * 30)
print("Matriz após a troca:\n", matriz_nova)