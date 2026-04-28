import numpy as np
sensores = np.array(((5, 1, 4, 6), (2, 0, 5, 3), (2, 2, 8, 7), (6, 2, 9, 3)))
sensores[:] = 1
print(sensores)