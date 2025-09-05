import numpy as np

class Matrix:
    matrix_objects={

    }
    def __init__(self, components, name):
        self.components=components
        self.name=name
    
    def matrix_construct(self):
        self.components=np.array(self.components)

    def matrix_object_saver(self):
        Matrix.matrix_objects[self.name]=self

    def matrix_list():
        for name,object in Matrix.matrix_objects.items():
            print(f"{object}")
        return ""
    
    def __str__(self):
        return f"{self.name} =\n{self.components}"
    
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
    Matrix.matrix_construct(M)
    Matrix.matrix_object_saver(M)
    Matrix.matrix_construct(N)
    Matrix.matrix_object_saver(N)    
    Matrix.matrix_list()
    
