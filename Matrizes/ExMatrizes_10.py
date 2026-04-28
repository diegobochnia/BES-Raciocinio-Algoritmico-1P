# 10.Matriz Transposta: Escreva um programa que receba uma matriz M x N e
# gere a sua transposta (N x M).

import numpy as np

matriz = np.array([
    [22, 57, 11, 84],
    [39,  6, 73, 42],
    [95, 18, 50, 61],
    [39,  6, 73, 42]
])

matriz_transposta = matriz.T

print(matriz)
print()
print(f"A matriz acima transposta é: \n", matriz_transposta)
