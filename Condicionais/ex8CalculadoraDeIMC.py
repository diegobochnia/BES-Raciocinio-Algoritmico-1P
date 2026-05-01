peso = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura em m: "))

imc = (peso / altura**2)
print("Seu IMC é: ", imc)
if imc > 25:
    print("Acima do peso ideal.")
else:
    print("Peso dentro da normalidade.")

# Estrutura condicional composta (if e else).
