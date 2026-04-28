import numpy as np
manha = (10, 12, 55, 0, 23)
tarde = (24, 0, 0, 0, 15)

chuva_manha = np.array(manha)
chuva_tarde = np.array(tarde)

chuva_total = chuva_manha + chuva_tarde

print("Quantidade de chuva registrada no período da manhã no dia 25/04: ", chuva_manha)
print("Quantidade de chuva registrada no período da tarde no dia 25/04: ", chuva_tarde)
print("-"*85)
print("Quantidade total de chuva do dia 25/04: ", chuva_total)