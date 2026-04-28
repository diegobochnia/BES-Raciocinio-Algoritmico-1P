# 10. Crie um dicionário com alguns dados. Peça ao usuário uma chave
# para remover usando pop(). Em seguida, remova um item com
# popitem(). Depois, peça novos dados ao usuário e atualize o
# dicionário com update(). Exiba o dicionário final.

precos = {"monitor": 850.00, "teclado": 120.50, "mouse": 89.90, "headset": 250.00, "pendrive": 45.00}
print(precos)
remover = input("Digite o nome do produto que deseja remover: ")
precos.pop(remover)
precos.popitem()
novo_produto = input("Digite o novo prodto que deseja inserir: ")
novo_valor = float(input(f"Digite o valor do produto: {novo_produto}: "))
precos.update({novo_produto: novo_valor})
print(precos)