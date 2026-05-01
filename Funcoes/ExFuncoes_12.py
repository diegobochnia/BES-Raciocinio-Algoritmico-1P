# 12. Modifique para aceitar valor padrão e valor informado.

def saudacao(nome, periodo='dia'):
    print(f"Bom {periodo}, {nome}!")

saudacao("Diego")
saudacao("Diego", "tarde")