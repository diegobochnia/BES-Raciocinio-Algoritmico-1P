# 11. Escreva um programa que remova as duplicatas de uma lista, garantindo que a ordem original dos primeiros elementos encontrados seja mantida.

numeros = [1, 2, 1, 2, 4, 3, 2, 3, 4]
resultado = []

for num in numeros:
    if num not in resultado:
        resultado.append(num)


print(resultado)