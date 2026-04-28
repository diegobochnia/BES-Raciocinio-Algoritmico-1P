# 9. Crie um dicionário com produtos e preços. Mostre ao usuário todas
# as chaves, todos os valores e todos os pares chave–valor.

precos = {"monitor": 850.00, "teclado": 120.50, "mouse": 89.90, "headset": 250.00, "pendrive": 45.00}

print(f"Chaves: \n", list(precos.keys()))
print(f"Valores: \n", list(precos.values()))
print("\nPares chave-valor:")
for produto, preco in precos.items():
    print(f"Produto: {produto} -> Preço: R$ {preco:.2f}")