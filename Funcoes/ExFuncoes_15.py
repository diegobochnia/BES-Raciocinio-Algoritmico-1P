# 15. Crie uma função mostrar_dados(**dados).

def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")

mostrar_dados(nome="Diego", idade=17, cidade="CWB")
