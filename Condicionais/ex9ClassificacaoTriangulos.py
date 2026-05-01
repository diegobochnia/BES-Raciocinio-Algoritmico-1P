lado1 = float(input("Digite a medida do primeiro lado do triângulo: "))
lado2 = float(input("Digite a medida do segundo lado do triângulo: "))
lado3 = float(input("Digite a medida do terceiro lado do triângulo: "))

if lado3 == lado2 == lado1:
    print("Equilátero.")
elif lado1 != lado2 != lado3:
    print("Escaleno.")
else:
    print("Isósceles")

# Estrutura condicional aninhada (condicional dentro de outra condicional).