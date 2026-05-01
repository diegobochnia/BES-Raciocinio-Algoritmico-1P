temperatura= int(input("Digite a temperatura em Celsius: "))
escolha = input("Você quer converter para Fahrenheit (F) ou Kelvin (K)?")
if escolha == "F":
    temperaturaF = (temperatura * (9/5)) + 32
    print(f"A temperatura {temperatura}ºC convertida para F é de {temperaturaF}")
elif escolha == "K":
    temperaturaK = temperatura + 273.15
    print(f"A temperatura {temperatura}ºC convertida para K é de {temperaturaK}")
else:
    print("Escolha inválida.")



# Estrutura condicional aninhada (condicional dentro de outra condicional).