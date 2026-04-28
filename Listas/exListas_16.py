# 16. Dadas duas listas, encontre a interseção entre elas (os elementos que estão presentes em ambas) sem usar a conversão para conjuntos (set).

lista1 = [1, 3, 5, 7, 9, 11, 13, 15]
lista2 = [3, 6, 9, 12, 15]

interseccao = []

for num in lista1:
    if num in lista2:
        interseccao.append(num)

print(interseccao)