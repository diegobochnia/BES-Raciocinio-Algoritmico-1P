# 12. Encontre o maior e o menor número em uma lista de inteiros sem usar as funções nativas max() e min().

numeros = [10, 2, 546, 113, 256000]
numeros_ordenados = sorted(numeros)
maiorNum = numeros_ordenados[-1]
menorNum = numeros_ordenados[0]

print("O maior número da lista é: ", maiorNum)
print("O menor número da lista é: ", menorNum)