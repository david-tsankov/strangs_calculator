import numpy as np

class Matrix_Manager:
    matrix_objects={

    }
    def __init__(self, components, name):
        self.components=components
        self.name=name
    
    def matrix_construct(self):
        self.components=np.array(self.components)

    def matrix_object_saver(self):
        Matrix_Manager.matrix_objects[self.name]=self

    def matrix_list():
        for name,object in Matrix_Manager.matrix_objects.items():
            print(f"{object}")
        return ""
    
    def __str__(self):
        return f"{self.name} =\n{self.components}"
    
    def matrix_multiplication(self, other: "Matrix_Manager",name_product: str="Matrix Multiplication"):
        product=np.matmul(self.components, other.components)
        product_object=Matrix_Manager(product,name_product)
        Matrix_Manager.matrix_object_saver(product_object)
        return product_object

    def get_geterminant(self):
        if self.components.shape[0]==self.components.shape[1]:
            det=np.linalg.det(self.components)
            return round(det,2)
        else:
            return "Please enter a square matrix!"
        
    def get_inverse(self):
        if np.linalg.det(self.components)==0:
            return "Matrix is singular, no inverse!"
        else:
            inverse=np.linalg.inv(self.components)
            return inverse
        
    def check_singularity(self):
        if round(np.linalg.det(self.components),2)==0:
            return "Matrix is singular (det=0)"
        else:
            return "Matrix is not singular (det!=0)"
        
    def get_rank(self):
        rank=np.linalg.matrix_rank(self.components)
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
        eigen_tupple=np.linalg.eig(self.components)
        for index in range(len(eigen_tupple[0])):
            print(f"Eigenvalue: {round(eigen_tupple[0][index],2)},\nEigenvector: \n{np.transpose(np.array([eigen_tupple[1][index]]))}\n")
        return "Eigenvectors are not saved in the memory, if you wish to use one to compute, you must create it separately!"
    
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
    M = Matrix_Manager([[5,2,0],[2,5,0],[-3,4,6]],"M")
    N = Matrix_Manager([[2,3,4],[9,3,-2],[0,3,6]],"N")
    Matrix_Manager.matrix_construct(M)
    Matrix_Manager.matrix_object_saver(M)
    Matrix_Manager.matrix_construct(N)
    Matrix_Manager.matrix_object_saver(N)    
    Matrix_Manager.matrix_list()
    print(Matrix_Manager.get_eigenvalues(M))
    
