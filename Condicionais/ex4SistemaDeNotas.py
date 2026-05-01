nota = float(input("Digite sua nota: "))
if nota >= 9.0:
    print("Parabéns!! Você esta aprovado!")
elif 7.0 < nota < 8.9:
    print("Aprovado.")
elif 4.0 < nota < 6.9:
    print("Em recuperação.")
else:
    print("Reprovado")

# Estrutura condicional aninhada (condicional dentro de outra condicional).