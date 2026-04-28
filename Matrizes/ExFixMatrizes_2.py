import numpy as np
inicial = ((100, 20, 580), (50, 50, 90), (1000, 5000, 500))
vendido = ((84, 18, 200), (40, 10, 89), (545, 3783, 500))
estoque_inicial = np.array(inicial)
total_vendido = np.array(vendido)
estoque_final = estoque_inicial - total_vendido

print("Estoque inicial: \n", estoque_inicial)
print("Vendido: \n", total_vendido)
print("-" * 50)
print("Estoque Final: \n", estoque_final)