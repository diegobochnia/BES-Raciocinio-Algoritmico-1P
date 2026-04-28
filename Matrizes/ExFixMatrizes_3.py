import numpy as np
ingredientes = ((3, 5, 8), (3, 4, 6))
pedidos = ((50, 10), (2, 152), (12, 22))

matriz_ingredientes = np.array(ingredientes)
matriz_pedidos = np.array(pedidos)
total_ingredientes = np.dot(matriz_ingredientes, matriz_pedidos)

print("Total de ingredientes para cada lanche: \n", matriz_ingredientes)
print("Total de pedidos de cada lanche: \n", matriz_pedidos)
print("-" * 50)
print("Resultado da multiplicação: \n", total_ingredientes)