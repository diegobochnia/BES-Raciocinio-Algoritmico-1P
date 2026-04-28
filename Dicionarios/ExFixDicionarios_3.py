# 3. Crie um dicionário vazio. Solicite ao usuário um nome e uma idade
# e armazene essas informações no dicionário como chave e valor.
# Exiba o dicionário ao final.

dados = {}
nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))

dados = dict(nome=nome, idade=idade)

print(dados)