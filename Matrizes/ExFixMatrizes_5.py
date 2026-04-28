# 5. Você está reiniciando um sistema que armazena dados temporários.
# Para limpar tudo, precisa zerar a matriz.
# Crie:
# • Uma matriz 3x3 com valores quaisquer.
# • Transforme todos os valores da matriz em 0.
# • Exiba a matriz final.
import numpy as np
dados = np.array(((5000, 1000, 546384), (2000, 1520, 4156), (1200, 2200, 1515)))
dados[:] = 0

print(dados)