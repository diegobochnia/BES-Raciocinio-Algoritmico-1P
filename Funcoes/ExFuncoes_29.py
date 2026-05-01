# 29. Crie calculadora(a, b, operacao).

def calculadora(a, b, operacao):
    return operacao(a, b)

soma = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero"


print(f"Soma: {calculadora(10, 5, soma)}")
print(f"Multiplicação: {calculadora(10, 5, multiplicacao)}")
print(f"Divisão: {calculadora(10, 5, divisao)}")