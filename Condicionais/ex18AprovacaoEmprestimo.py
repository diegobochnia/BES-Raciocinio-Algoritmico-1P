valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Em quantos anos você irá pagar? "))
prestMensal = valorCasa / (anos * 12)
if prestMensal <= (salario * 0.3):
    print("Empréstimo Aprovado!")
else:
    print("Empréstimo negado.")


# Estrutura condicional composta (if e else).
