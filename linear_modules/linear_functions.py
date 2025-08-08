import numpy as np
import class_matrices as class_M
import class_vectors as class_V



def solve_system_of_equations(self: "class_M", other: "class_V"):
    """Computes exact solution of equations of the sort Ax=b, where A is the first parameter, and b is the second parameter."""
    x=np.linalg.solve(self.matrix,other.vector)
    return x



if __name__ == "__main__":
    A=class_M.Matrix([[1,-3,0],[3,1,-1],[9,-2,1]])
    class_M.Matrix.matrix_construct(A)
    print(A)
    b=class_V.Vector([[4],[5],[-2]])
    class_V.Vector.vector_construct(b)
    print(b)
    x=solve_system_of_equations(A,b)
    print(x)