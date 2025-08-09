import numpy as np
from .class_matrices import Matrix
from .class_vectors import Vector

def solve_system_of_equations(self: "Matrix", other: "Vector"):
    """Computes exact solution of equations of the sort Ax=b, where A is the first parameter, and b is the second parameter."""
    if np.linalg.det(self.matrix)!=0:
        x=np.linalg.solve(self.matrix,other.vector)
        return x
    elif np.linalg.det(self.matrix)==0:
        return "Matrix is singular (det=0), please enter a non-singular matrix!"



if __name__ == "__main__":
    M=Matrix([[1,2,3],[4,5,6],[7,-2,9]])
    M.matrix_construct()
    print(M.check_singularity())
    b=Vector([[3],[2],[1]])
    b.vector_construct
    x=solve_system_of_equations(M,b)
    print(x)