#1. Cadastro de números inteiros
#Crie um programa em Python que:
#• Solicite ao usuário a entrada de 10 números inteiros;
# Armazene esses valores em uma lista chamada a.

a = []
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    a.append(numero)

#2. Exibição de elementos da lista
#Considerando a lista a do exercício anterior, crie um programa que:
#• Exiba todos os elementos da lista na tela;
#• Mostre os valores um por linha.

for numero in a:
    print(numero)