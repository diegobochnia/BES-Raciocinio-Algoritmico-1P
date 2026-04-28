# 15.Rotação 90°: Crie um algoritmo que rotaciona uma matriz quadrada n x n em
# 90 graus no sentido horário (sem usar bibliotecas prontas como NumPy)


matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

n = len(matriz)
matriz_rotacionada = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        matriz_rotacionada[j][n - 1 - i] = matriz[i][j]

for linha in matriz_rotacionada:
    print(linha)