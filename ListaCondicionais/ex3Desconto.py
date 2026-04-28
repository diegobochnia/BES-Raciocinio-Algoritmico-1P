valorTotal = float(input("Digite o valor total da compra: "))
if valorTotal > 100:
    valorComDesconto = valorTotal * 0.9
    print("O valor final com desconto é de: R$", valorComDesconto)
else:
    print("O valor final é de: R$ ", valorTotal)

# Estrutura condicional composta (if e else).