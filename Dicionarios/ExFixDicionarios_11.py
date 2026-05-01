
usuarios = {
    "Ana": 25,
    "João": 32,
    "Beatriz": 19,
    "Carlos": 45,
    "Mariana": 17,
    "Ricardo": 60,
    "Fernanda": 22
}

def menu():
    print("MENU".center(40))
    print("[1] Exibir todos os usuários cadastrados")
    print("[2] Buscar usuário")
    print("[3] Adicionar usuário")
    print("[4] Atualizar idade")
    print("[5] Remover usuário")
    print("[6] Remover o último elemento inserido")
    print("[7] Gerenciar cópias")
    print("[8] Inicializar um novo dicionário (fromkeys())")
    print("[9] Atualizar o dicionário principal")
    print("[10] Limpar todos os dados do sistema")
    print("[11] Criar um novo dicionário (dict())")
    print("[12] Sair")

def exibir_usuario():
    while True:
        print("Opção 1: \nEXIBIR TODOS OS USUÁRIOS CADASTRADOS, MOSTRANDO:")
        print("[1] Apenas os nomes")
        print("[2] Apenas as idades")
        print("[3] Todos os pares nome-idade")
        print("[0] Voltar ao Menu Principal")
        opcao1 = int(input("Escolha uma opção para prosseguir: "))

        if opcao1 == 1:
            print("NOMES DOS USUÁRIOS CADASTRADOS: \n\n", list(usuarios.keys()),"\n")

        elif opcao1 == 2:
            print("IDADE DOS USUÁRIOS: \n\n", list(usuarios.values()), "\n")

        elif opcao1 == 3:
            print("Todos os pares NOME-IDADE dos usuários cadastrados: \n")
            for nome, idade in usuarios.items():
                print(f"Usuário: {nome} | Idade: {idade} anos.")
            print()

        elif opcao1 == 0:
            print("Voltando ao Menu Principal...\n")
            break

        else:
            print("Opção inválida, escolha outra opção: ")

def buscar_usuario():
    while True:
        print("\nOpção 2: \nBUSCAR USUÁRIO PELO NOME:")
        nome_input = input("Digite o nome do usuário (ou 0 para voltar): ").strip()

        if nome_input == "0":
            break

        nome_busca = nome_input.capitalize()

        idade = usuarios.get(nome_busca)

        if idade is not None:
            print("Usuário encontrado!")
            print(f"Nome: {nome_busca} | Idade: {idade} anos.")

        else:
            print(f"Erro: O usuário '{nome_busca}' não está cadastrado.")

def adiciona_usuario():
    while True:
        print("Opção 3: \nAdicionar um novo usuário: ")
        nome_novo_usuario = input("Digite o nome do novo usuário (ou 0 para voltar): ")

        if nome_novo_usuario == "0":
            break

        elif nome_novo_usuario in usuarios:
            print(f"Erro: O usuário {nome_novo_usuario} já está cadastrado!")

        else:
            idade_novo_usuário = int(input("Digite a idade do novo usuário: "))
            usuarios[nome_novo_usuario] = idade_novo_usuário
            print("Usuário cadastrado com sucesso!")

def atualiza_idade():
    while True:
        print("Opção 3: \nAtualizar a idade de um usuário: ")
        usuario_atualizar = input("Digite o nome do usuário (ou 0 para voltar): ").capitalize()

        if usuario_atualizar == "0":
            break

        elif usuario_atualizar not in usuarios:
            print("Usuário não cadastrado!")

        else:
            idade_atualizar_usuario = int(input(f"Digite a nova idade do usuário {usuario_atualizar}: "))
            usuarios[usuario_atualizar] = idade_atualizar_usuario
            print("Idade atualizada com sucesso!")

def remove_usuario():
    while True:
        print("Opção 5: \nRemover um usuário: ")
        usuario_remove = input("Digite o nome do usuário (ou 0 para voltar): ").capitalize()

        if usuario_remove == "0":
            break

        elif usuario_remove not in usuarios:
            print("Usuário não encontrado.")

        else:
            print(f"Tem certeza que quer remover permanentemente o usuário {usuario_remove}?")
            tem_certeza = int(input("[1] Sim \n[2] Não \nEscolha uma opção: "))
            if tem_certeza == 1:
                usuarios.pop(usuario_remove)
                print("Usuário removido com sucesso!")

            else:
                break

def remove_ultimo_inserido():
    while True:
        print("Opção 6: \nRemover o ultimo elemento inserido: ")
        tem_certeza = int(input("Tem certeza que quer remover permanentemente o último elemento inserido? \n[1] Sim \n[2] Não \nEscolha uma opção: "))

        if tem_certeza == 1:
            usuarios.popitem()
            print("Último elemento removido com sucesso!")
            break

        else:
            break

def criar_copia():
    copia_usuários = None

    while True:
        print("Opção 7: \nGERENCIAR CÓPIA:")
        print("[1] Criar cópia do dicionário \n[2] Alterar valor na cópia \n[3] Comparar original vc Cópia \n[0] Voltar ao Menu Principal")
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            copia_usuarios = usuarios.copy()
            print("\nDicionário copiado com sucesso!\n")

        elif escolha == 2:
            if copia_usuarios is None:
                print("Erro: Você precisa criar a cópia primeiro.")

            else:
                nome = input("Digite o nome do usuário para alterar o valor: ").strip().capitalize()
                if nome in copia_usuarios:
                    nova_idade = int(input(f"Digite a nova idade para o usuário {nome} na cópia: "))
                    copia_usuarios[nome] = nova_idade
                    print(f"\nIdade de {nome} alterada apenas na cópia.\n")

                else:
                    print("Usuário não encontrado na cópia.")

        elif escolha == 3:
            if copia_usuarios is None:
                print("Erro: Nenhuma cópia foi criada ainda.")

            else:
                print("\nDICIONÁRIO ORIGINAL".center(20))
                for c, v in usuarios.items():
                    print(f"{c}: {v}")

                print("\nDICIONÁRIO CÓPIA".center(20))
                for c, v in copia_usuarios.items():
                    print(f"{c}: {v}")
                print()

        elif escolha == 0:
            print("voltando ao Menu Principal")
            break

        else:
            print("Opção inválida")

def novo_dicionario_fromkeys():
    while True:
        print("Opção 8: \nINICIALIZAR UM NOVO DICIONÁRIO (fromkeys())")
        nomes = input("Digite uma lista de nomes separados por vírgula Ex(....., ....., ....., .....): ")
        idade = int(input("Digite a idade padrão para todos os usuários: "))

        nomes_separados = [nome.strip() for nome in nomes.split(",")]
        usuarios_novo = dict.fromkeys(nomes_separados, idade)
        print("Dicionário criado com sucesso!\n")

        for c, v in usuarios_novo.items():
            print(f"{c}: {v}")

        voltar = int(input("\nDigite 0 para voltar ao Menu Principal: "))
        if voltar == 0:
            break

def atualizar_dicionario_principal():
    print("Opção 9: \nAtualizar o dicionário principal: ")
    novos_dados = {}

    while True:
        nome = input("Digite o nome do usuário para atualizar/adicionar (ou 0 para sair): ").strip().capitalize()

        if nome == "0":
            break

        idade = int(input(f"Digite a idade para {nome}: "))

        novos_dados[nome] = idade

    if novos_dados:
        usuarios.update(novos_dados)
        print("Dicionário principal atualizado com sucesso!")

    else:
        print("Nenhuma alteração realizada.")

def limpa_sistema():
    while True:
        print("Opção 10: \nLimpar todos os dados do sistema:")
        confirma = int(input("Tem certeza que deseja limpar todos os dados do sistema? \n[1] Sim \n[2] Não, voltar \nEscolha uma opção: "))

        if confirma == 1:
            usuarios.clear()
            print("\nTodos os dados foram removidos com sucesso!\n")
            break


        elif confirma == 2:
            print("Voltando ao menu Principal")
            break

        else:
            print("Opção inválida")

def novo_dicionario_dict():
    print("Opção 11: \nCriar um novo dicionário")
    lista_temporaria = []

    while True:
        nome = input("Digite o nome (ou 0 para sair): ").strip().capitalize()

        if nome == "0":
            break

        idade = int(input(f"Digite a idade de {nome}: "))

        usuario = (nome, idade)
        lista_temporaria.append(usuario)

    if lista_temporaria:
        novo_dicionario = dict(lista_temporaria)
        print("Novo dicionário criado com sucesso!")
        print(novo_dicionario)

    else:
        print("Nenhum dado informado.")

while True:
    menu()
    opcao = int(input("Escolha uma opção para prosseguir: "))

    if opcao == 1:
        exibir_usuario()
    elif opcao == 2:
        buscar_usuario()
    elif opcao == 3:
        adiciona_usuario()
    elif opcao == 4:
        atualiza_idade()
    elif opcao == 5:
        remove_usuario()
    elif opcao == 6:
        remove_ultimo_inserido()
    elif opcao == 7:
        criar_copia()
    elif opcao == 8:
        novo_dicionario_fromkeys()
    elif opcao == 9:
        atualizar_dicionario_principal()
    elif opcao == 10:
        limpa_sistema()
    elif opcao == 11:
        novo_dicionario_dict()
    elif opcao == 12:
        print("Até mais!")
        break
    else:
        print("Opção inválida")