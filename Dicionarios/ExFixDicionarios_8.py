# 8. Crie um dicionário com alguns alunos e suas notas. Peça ao
# usuário o nome de um aluno e utilize get() para buscar a nota. Caso
# o aluno não exista, exiba uma mensagem padrão.

notas = {"alice": 9.5, "bruno": 7.0, "carla": 8.5, "daniel": 6.5}
nome = input("Digite o nome de um aluno para buscar a nota: ").lower()

nota = notas.get(nome, "O aluno não existe.")

print(nota)

