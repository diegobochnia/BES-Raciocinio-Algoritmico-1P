# 9. Chame a função acima (ex 8) usando argumentos posicionais e nomeados.

def apresentar(nome, idade, cidade):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

apresentar("Diego", 17, "CWB")
apresentar(nome="Diego", idade=17, cidade="CWB")