import numpy as np

class Matrix:
    matrices={

    }
    def __init__(self, matrix, name):
        self.matrix=matrix
        self.name=name
    
    def matrix_construct(self):
        self.matrix=np.array(self.matrix)
        Matrix.matrices[self.name]=self.matrix.tolist()

    def matrix_list():
        for name, matrix in Matrix.matrices.items():
            print(f"{name}")
            for row in matrix:
                print(f"{row}")
    
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
            return "Please enter a square matrix!"
        
    def get_inverse(self):
        if np.linalg.det(self.matrix)==0:
            return "Matrix is singular, no inverse!"
        else:
            inverse=np.linalg.inv(self.matrix)
            return inverse
        
    def check_singularity(self):
        if np.linalg.det(self.matrix)==0:
            return "Matrix is singular (det=0)"
        else:
            return "Matrix is not singular (det!=0)"
        
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
        return "Eigenvectors are horizontal in this functions output!"
    
    def get_cayley_hamilton_equation(self):
        pass

    # def get_column_space():
    #     pass

    # def get_basis_for_column_space():
    #     pass

    def get_nullspace():
        pass

    def get_elimination_matrix():
        pass

        
    

if __name__=="__main__":
    M = Matrix([[-2,2,0],[-1,1,0],[3,0,1]],"M")
    N = Matrix([[2,3,4],[9,3,-2],[0,3,6]],"N")
    M.matrix_construct()
    N.matrix_construct()
    Matrix.matrix_list()
    
