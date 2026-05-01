 # 27. Crie função media(lista) com docstring.

def media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

numeros = [10, 20, 30, 40]
resultado = media(numeros)

print("A média é: ", resultado)

# 28. Use help() para exibir a documentação.

help(media)