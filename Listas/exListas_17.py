# 17. "Achate" (flatten) uma lista de listas (uma matriz bidimensional) em uma única lista unidimensional (Exemplo: [[1, 2], [3, 4]] vira [1, 2, 3, 4]).

matriz = [[1, 2], [3, 4], [5, 6]]
achatada = []

for sublista in matriz:
    achatada += sublista

print(achatada)