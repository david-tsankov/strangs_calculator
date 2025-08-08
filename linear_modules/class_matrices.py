import numpy as np
from class_vectors import Vector

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
    
    def matrix_construct(self):
        self.matrix=np.array(self.matrix)
        return self.matrix
    
    def __str__(self):
        return f"{self.matrix}"
    
    def matrix_multiplication(self, other: "Matrix"):
        product=np.matmul(self.matrix, other.matrix)
        return product

    def get_geterminant(self):
        if self.matrix.shape[0]==self.matrix.shape[1]:
            det=np.linalg.det(self.matrix)
            return det
        else:
            return f"Please enter a square matrix!"
        
    def get_inverse(self):
        if np.linalg.det(self.matrix)==0:
            return f"Matrix is singular, no inverse!"
        else:
            inverse=np.linalg.inv(self.matrix)
            return inverse
        
    def check_singularity(self):
        if np.linalg.det(self.matrix)==0:
            return f"Matrix is singular (det=0)"
        else:
            return f"Matrix is not singular (det!=0)"
        
    def get_rank(self):
        rank=np.linalg.matrix_rank(self.matrix)
        superscripts = {
            1: "\u00B9",
            2: "\u00B2",
            3: "\u00B3",
            4: "\u2074",
            5: "\u2075",
            6: "\u2076",
            7: "\u2077",
            8: "\u2078",
            9: "\u2079",
            10: "\u00B9\u2070"
        }
        return f"{rank}, or R{superscripts[rank]}"
    
    def get_eigenvalues(self):
        eigen_tupple=np.linalg.eig(self.matrix)
        for index in range(len(eigen_tupple[0])):
            print(f"Eigenvalue: {eigen_tupple[0][index]}, Eigenvector: {eigen_tupple[1][index]}")
        return f"Eigenvectors are horizontal in this functions output!"
    
    def get_cayley_hamilton_equation(self):
        pass
        
    

if __name__=="__main__":
    M = Matrix([[-2,2,0],[-1,1,0],[3,0,1]])
    N = Matrix([[2,3,4],[9,3,-2],[0,3,6]])
    M.matrix_construct()
    N.matrix_construct()
    # print(M)
    # print(N)
    # product=Matrix.matrix_multiplication(N,M)
    # product2=Matrix.matrix_multiplication(M,N)
    # print(product)
    # print(product2)

    # Determinant test
    # A=Matrix([[1,0,0],[0,1,0],[0,0,1]])
    # A.matrix_construct()
    # B=Matrix([[1,0,0],[0,1,0]])
    # B.matrix_construct()
    # print(A.get_geterminant())
    # print(B.get_geterminant())
    # print(M.get_inverse())

    print(M.get_rank())
    print(M.get_eigenvalues())
