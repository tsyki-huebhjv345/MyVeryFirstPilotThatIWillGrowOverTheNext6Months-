import numpy as np
from qiskit.visualization import array_to_latex
#task_1
ket_0=np.array([[1],[0]])
ket_1=np.array([[0],[1]])

#print (ket_0/2 + ket_1/2)

#task_2
M1=np.array([[1, 1],[0, 0]])
M2=np.array([[1, 0],[0, 1]])
M = M1/2 + M2/2#50/50 chance to each of matrices

#task_3
print(M1 @ ket_0)
print(M1 @ M2)
print(M @ M)

#task_4
display(array_to_latex(M1 @ ket_1))

