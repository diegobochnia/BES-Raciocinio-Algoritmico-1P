# 7. Concatene as listas lista1 = [1, 2] e lista2 = [3, 4] em uma terceira lista.

lista1 = [1, 2]
lista2 = [3, 4]

lista3 = lista1.copy()
lista3.extend(lista2)

print(lista3)