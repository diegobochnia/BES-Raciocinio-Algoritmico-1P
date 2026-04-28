# 6. Crie um dicionário com alguns dados. Faça uma cópia desse
# dicionário. Em seguida, altere um valor na cópia e mostre os dois
# dicionários para comparar.

dados = {'nome': 'Diego', 'idade': '17', 'cidade': 'CWB'}
dados_copia = dados.copy()
dados_copia['idade'] = 18

print(dados)
print("-" * 50)
print(dados_copia)