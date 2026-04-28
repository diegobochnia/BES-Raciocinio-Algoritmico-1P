# 4. Peça ao usuário para informar três pares de dados (chave e valor).
# Utilize a função dict() para construir o dicionário e exiba o resultado.

dicionario = {}

for i in range(3):
    chave = input(f"Digite a chave {i+1}: ")
    valor = input(f"Digite o valor para a chave {i+1}: ")
    dicionario[chave] = valor

print(dicionario)