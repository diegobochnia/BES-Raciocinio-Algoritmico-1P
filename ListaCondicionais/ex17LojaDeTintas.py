area = float(input("Digite o tamanho em m² da área a ser pintada: "))
cont = 0
if area <= 54:
    print("Você precisará de apenas 1 lata de tinta, R$ 80,00")
else:
    while area > 54:
        area = area - 54
        cont = cont + 1
    if area > 0:
        cont = cont + 1
    print(f"Você precisará de {cont} latas de tinta, RS {cont * 80.00}")


# Estrutura condicional aninhada (condicional dentro de outra condicional).