alunosTurma = []
nAlunos = int(input("Digite o número de alunos da turma: "))

for i in range(nAlunos):
    nome = input("Digite o nome do aluno: ")
    alunosTurma.append(nome)
print("Os alunos da turma são: ")
for nome in alunosTurma:
    print(nome)