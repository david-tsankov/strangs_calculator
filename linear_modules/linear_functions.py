import numpy as np
import sympy as sp
import class_matrices as Matrix
import class_vectors as Vector

# def get_column_space():
#     pass

# def get_basis_for_column_space():
#     pass

# def get_nullspace():
#     pass

def get_elimination_matrix():
    pass

def get_cayley_hamilton_equation():
    pass

def solve_system_of_equations(self: "Matrix", other: "Vector"):
    """Computes exact solution of equations of the sort Ax=b, where A is the first parameter, and b is the second parameter."""
    x=np.linalg.solve(self.matrix,other.vector)
    return x



if __name__ == "__main__":
    A=Matrix.Matrix([[1,0,0],[0,1,0],[0,0,1]])
    Matrix.Matrix.matrix_construct(A)
    print(A)
    b=Vector.Vector([[4],[5],[-2]])
    Vector.Vector.vector_construct(b)
    print(b)
    x=solve_system_of_equations(A,b)
    print(x)