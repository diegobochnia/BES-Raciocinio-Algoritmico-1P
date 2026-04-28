# 7. Solicite ao usuário uma lista de nomes (separados por vírgula).
# Utilize fromkeys() para criar um dicionário onde todas as chaves
# sejam esses nomes e o valor padrão seja 0.

nomes = input("Digite uma lista de nomes separados por vírgula Ex(....., ....., ....., .....): ")
nomes_separados = [nome.strip() for nome in nomes.split(",")]
dicionario = dict.fromkeys(nomes_separados, 0)
print(dicionario)