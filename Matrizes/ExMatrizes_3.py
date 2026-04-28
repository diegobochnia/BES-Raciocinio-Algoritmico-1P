# 3. Busca Simples: Dada uma matriz 4 x 4, peça um número ao usuário e diga
# se esse número está ou não na matriz.

import numpy as np
matriz4x4 = np.array((
    (15, 82, 43, 29),
    (61,  7, 94, 52),
    (38, 70, 11, 85),
    (49, 26, 63,  5)
))
num = int(input("Digite um número inteiro: "))
if num in matriz4x4:
    print(f"O número {num} faz parte da matriz.")
else:
    print(f"O número {num} não faz parte da matriz.")