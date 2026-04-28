# 2. Crie um dicionário com o preço de três produtos. Peça ao usuário
# qual produto deseja alterar e o novo preço. Atualize o dicionário e
# exiba o resultado.

precos = {"produto 1" : 10.00, "produto 2" : 49.90, "produto 3" : 2.99}

produto = input("Escolha um produto para alterar o preço: \nproduto 1 \nproduto 2 \nproduto 3 \nDigite a sua escolha: ")
novo_preco = float(input("Digite o novo valor: "))
precos[produto] = novo_preco

print(precos)