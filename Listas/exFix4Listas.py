#4. Análise de notas de alunos
#Crie um programa em Python que:
#• Solicite ao usuário a quantidade de alunos da turma;
#• Em seguida, leia a nota de cada aluno (valores inteiros de 0 a
#100);
#• Armazene as notas em uma lista;
#• Ao final, informe:
#• Quantos alunos estão abaixo da média;
#• Quantos alunos estão na média ou acima.
#Considere:
#• Média = 60.
alunosAprovados = 0
alunosReprovados = 0
QtdAlunos = int(input("Digite a quantidade de alunos da turma: "))
notas = []
for i in range(QtdAlunos):
    nota = int(input(f"Digite a nota do aluno {i+1} (0 a 100): "))
    notas.append(nota)

for nota in notas:
    if nota >= 60:
        alunosAprovados += 1
    else:
        alunosReprovados += 1
print(f"Alunos abaixo da média (menor que 60): {alunosReprovados}")
print(f"Alunos na média ou acima (60 ou mais): {alunosAprovados}")