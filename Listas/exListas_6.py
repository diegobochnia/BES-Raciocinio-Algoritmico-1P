# 6. Verifique se o número 7 está presente na lista valores = [1, 3, 5, 7, 9] e imprima o resultado booleano.

valores = [1, 3, 5, 7, 9]
resultado = False

for num in valores:
    if num == 7:
        resultado = True
        break

print(resultado)
