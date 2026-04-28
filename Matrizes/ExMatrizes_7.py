# 7. Maior Elemento: Crie uma matriz preenchida com números aleatórios e
# encontre qual é o maior valor presente nela.

import numpy as np

matriz = np.array((
    (22, 57, 11, 84),
    (39,  6, 73, 42),
    (95, 18, 50, 61)
))

maior_numero = np.max(matriz)

print(matriz)
print()
print("O maior número da matriz acima é: ", maior_numero)
