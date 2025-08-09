import numpy as np
from linear_modules.class_matrices import Matrix
from linear_modules.class_vectors import Vector
from linear_modules.matrix_and_vector_functions import solve_system_of_equations

print(f"{"Welcome to Strangs Calculator":^100}")
print(f"{100*"-"}")
print(f"{"Keep in mind to perform any operation you must first construct a vector/matrix!":^100}")
print(f"{100*"-"}")
print(f"{"Choose what operation you would like to perform:":^100}")
print(f"{"1 - Construct a vector":<25}{"2 - Construct a matrix":<25}{"3 - Transpose":<25}{"4 - Get lenght":<25}")

M=Matrix([[1,0,0],[0,1,0],[0,0,1]])
b=Vector([[1],[0],[0]])
M.matrix_construct()
b.vector_construct()
x=solve_system_of_equations(M,b)
print(x)

