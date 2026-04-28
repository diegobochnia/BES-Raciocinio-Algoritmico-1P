# Você encontrou um erro em um sistema: um valor específico da
# matriz está incorreto.
# Crie:
# • Uma matriz 5x5 com valores inteiros.
# • Substitua o valor das posições:
# • Linha 1, coluna 2.
# • Linha 3, coluna 5.
# • Defina novos valores para essas posições.
# • Exiba a matriz antes e depois da alteração.
import numpy as np
matriz_inteiros = np.array((
    (82, 15, 44, 91, 23),
    (67,  8, 56, 30, 74),
    (12, 99, 41,  5, 66),
    (38, 72, 19, 83, 10),
    (54, 21, 88, 47, 95)
))
print("Matriz antes da alteração:\n", matriz_inteiros)
matriz_inteiros[0][1] = 100
matriz_inteiros[2][4] = 100
print("-" * 30)
print("Matriz depois da alteração:\n", matriz_inteiros)