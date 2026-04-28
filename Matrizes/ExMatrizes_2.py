# 2. Identidade: Peça ao usuário um valor n e gere uma Matriz Identidade de
# ordem n.
import numpy as np
n = int(input("Digite um valor inteiro para n: "))

identidade = np.eye(n)
print(identidade)