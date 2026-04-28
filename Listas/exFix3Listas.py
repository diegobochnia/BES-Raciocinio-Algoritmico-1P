#3. Maior e menor valor
#Crie um programa em Python que:
#• Solicite ao usuário a entrada de 10 números inteiros;
#• Armazene esses valores em uma lista chamada a;
#• Ao final, informe:
#• O maior valor da lista;
#• O menor valor da lista.

a = []
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    a.append(numero)

menorValor = min(a)
maiorValor = max(a)

print("O menor número da lista é: ", menorValor)
print("O maior número da lista é: ", maiorValor)