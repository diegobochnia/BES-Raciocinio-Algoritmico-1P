# 5. Crie uma função dividir(a, b) que retorne o quociente e o resto da divisão.

def dividir(a, b):
    divisao = a // b
    resto = a % b
    print(f"{a} / {b} = ", divisao, resto)
dividir(10, 3)