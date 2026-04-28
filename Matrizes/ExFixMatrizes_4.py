import numpy as np
salarios = ((5000, 1000), (2000, 1520), (1200, 2200))
aumento = 1.10
salarios_arr = np.array(salarios)
salario_com_aumento = salarios_arr * aumento

print("Salário dos funcionários antes do aumento: \n", salarios_arr)
print("-" * 50)
print("Salário dos funcionários depois do aumento: \n", salario_com_aumento)