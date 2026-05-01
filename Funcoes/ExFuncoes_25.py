# 25. Crie contagem recursiva de n até 0.

def contagem(n):
    if n == 0:
        print("Fim!")
    else:
        print(n)
        contagem(n - 1)

contagem(10)
