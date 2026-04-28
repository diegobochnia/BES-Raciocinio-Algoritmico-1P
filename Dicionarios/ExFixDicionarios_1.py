# 1. Crie um dicionário com nome, idade e cidade de uma pessoa.
# Solicite ao usuário uma chave e exiba o valor correspondente.

dados = {"nome" : "Diego", "idade" : 17, "cidade" : "Curitiba"}
chave = input("Escolha uma das chaves a seguir: \n nome \n idade \n cidade \n Sua escolha: ")

print(f"{chave} = {dados[chave]}")