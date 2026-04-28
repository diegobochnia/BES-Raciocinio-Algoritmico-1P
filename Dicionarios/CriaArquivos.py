# criar_arquivos.py
prefixo = "ExFixDicionarios"
extensao = ".py"
quantidade = 12

for i in range(1, quantidade + 1):
    nome_arquivo = f"{prefixo}_{i}{extensao}"

    # 'w' cria o arquivo. Use 'with' para fechar automaticamente.
    with open(nome_arquivo, 'w') as f:
        f.write("# Arquivo gerado automaticamente\n")
        f.write(f"print('Este é o arquivo {i}')\n")

print(f"{quantidade} arquivos criados com sucesso.")
