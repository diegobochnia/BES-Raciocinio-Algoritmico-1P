# 5. Multiplicação por Escalar: Leia uma matriz 3 x 3 e um número real. Exiba a
# matriz resultante da multiplicação de cada elemento por esse número.
import numpy as np
linhas = 3
colunas = 3
matriz = []
for i in range(colunas):
    linha = []
    for j in range(linhas):
        num = int(input(f"Digite um número inteiro para a posição ({i}, {j}): "))
        linha.append(num)
    matriz.append(linha)

matriz = np.array(matriz)
print(matriz)
mult = int(input("Digite o némero pelo qual você deseja multiplicar a matriz anterior: "))

matriz_mult = matriz * mult
print(f"A matriz\n {matriz}, multiplicada por {mult} é: \n \n", matriz_mult)