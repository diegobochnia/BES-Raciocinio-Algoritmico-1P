# 5. Crie um dicionário com alguns elementos. Pergunte ao usuário se
# deseja apagar todos os dados. Caso a resposta seja 'sim', utilize
# clear() e mostre o dicionário final.

dicionario = {'nome': 'Diego', 'idade': '17', 'cidade': 'CWB'}
escolha = bool(int(input(f"Deseja apagar todos os dados do dicionário a seguir? \n {dicionario}\n Sim = 1 \n Não = 0 \n Digite a sua escolha: ")))
if escolha == True:
    dicionario.clear()
    print("Todos os dados do dicionário foram apagados!")
else:
    print(f"Nenhum dado fio apagado! \n {dicionario}")