#5. Análise de números inteiros
#Crie um programa em Python que:
#• Solicite ao usuário a entrada de 5 números inteiros;
#• Armazene esses valores em uma lista;
#• Ao final, determine e exiba:
#• O maior número par da lista (caso exista);
#• O menor número ímpar da lista (caso exista);
#• O somatório de todos os elementos da lista;
#• A média dos valores.
#• Caso não existam números pares ou ímpares, exiba uma mensagem apropriada.

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

soma = sum(numeros)
media = soma / len(numeros)

if pares:
    print(f"O maior número par é: {max(pares)}")
else:
    print("Não foram digitados números pares.")

if impares:
    print(f"O menor número ímpar é: {min(impares)}")
else:
    print("Não foram digitados números ímpares.")

print(f"Soma de todos os elementos: {soma}")
print(f"Média: {media}")