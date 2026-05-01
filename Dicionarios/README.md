### Exercícios de Fixação: Dicionários

1. **Acesso por Chave**: Crie um dicionário com `nome`, `idade` e `cidade` de uma pessoa. Solicite ao usuário uma chave e exiba o valor correspondente.

2. **Atualização de Preço**: Crie um dicionário com o preço de três produtos. Peça ao usuário qual produto deseja alterar e o novo preço. Atualize o dicionário e exiba o resultado.

3. **Dicionário Dinâmico**: Crie um dicionário vazio. Solicite ao usuário um nome e uma idade, armazene essas informações como chave e valor, e exiba o dicionário ao final.

4. **Construção com `dict()`**: Peça ao usuário para informar três pares de dados (chave e valor). Utilize a função `dict()` para construir o dicionário e exiba o resultado.

5. **Limpeza com `clear()`**: Crie um dicionário com alguns elementos. Pergunte ao usuário se deseja apagar todos os dados. Caso a resposta seja `'sim'`, utilize `clear()` e mostre o dicionário final.

6. **Cópia de Dicionário**: Crie um dicionário com alguns dados. Faça uma cópia com `copy()`. Em seguida, altere um valor na cópia e mostre os dois dicionários para comparar.

7. **Dicionário com `fromkeys()`**: Solicite ao usuário uma lista de nomes separados por vírgula. Utilize `fromkeys()` para criar um dicionário onde todas as chaves sejam esses nomes e o valor padrão seja `0`.

8. **Busca com `get()`**: Crie um dicionário com alguns alunos e suas notas. Peça ao usuário o nome de um aluno e utilize `get()` para buscar a nota. Caso o aluno não exista, exiba uma mensagem padrão.

9. **Iterando o Dicionário**: Crie um dicionário com produtos e preços. Mostre ao usuário todas as chaves com `keys()`, todos os valores com `values()` e todos os pares chave–valor com `items()`.

10. **Manipulação Completa**: Crie um dicionário com alguns dados e realize as operações abaixo em sequência:
    - Peça ao usuário uma chave e remova-a com `pop()`.
    - Remova o último item inserido com `popitem()`.
    - Solicite novos dados ao usuário e atualize o dicionário com `update()`.
    - Exiba o dicionário final.

11. **Sistema de Gerenciamento de Usuários**: Desenvolva um programa que simule um sistema de gerenciamento de usuários utilizando dicionários.

    O sistema deve iniciar com um dicionário contendo pelo menos 3 usuários, onde a chave representa o nome e o valor representa a idade. Ao iniciar, o programa exibe um menu de opções com as seguintes funcionalidades:

    - **Exibir usuários**: mostre apenas os nomes com `keys()`, apenas as idades com `values()`, e todos os pares nome–idade com `items()`.
    - **Buscar usuário**: pesquise pelo nome utilizando `get()`. Caso não exista, exiba uma mensagem apropriada.
    - **Adicionar usuário**: solicite nome e idade e insira diretamente no dicionário.
    - **Atualizar idade**: solicite o nome do usuário e a nova idade e atualize o registro.
    - **Remover usuário específico**: solicite o nome e remova com `pop()`.
    - **Remover último inserido**: remova o último elemento com `popitem()`.
    - **Copiar e comparar**: crie uma cópia com `copy()`, permita que o usuário altere um valor na cópia e exiba ambos os dicionários para comparação.
    - **Inicializar com `fromkeys()`**: solicite uma lista de nomes separados por vírgula e uma idade padrão, e crie um novo dicionário com `fromkeys()`.
    - **Atualizar com `update()`**: solicite novos pares de dados ao usuário e atualize o dicionário principal.
    - **Limpar dados**: apague todos os registros com `clear()`, mediante confirmação do usuário.
    - **Criar com `dict()`**: solicite uma lista de tuplas ao usuário e construa um novo dicionário com `dict()`.
    - **Sair**: encerre o programa.

    > O programa deve continuar executando até que o usuário escolha a opção de sair.