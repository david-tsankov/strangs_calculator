import numpy as np

class Vector:
    def __init__(self,vector):
        self.vector = vector

    def vector_contructor(self):
        self.vector=np.array(self.vector)

    def __str__(self):
        return f"{self.vector}"
    
    def get_lenght(self):
        norm=np.linalg.norm(self.vector)
        return norm
    
    def transpose(self):
        vector_transpose=np.transpose(self.vector)
        return vector_transpose
    
    def scalar_multiplication(self, scalar: float=1):
        new_vector=np.dot(self.vector, scalar)
        return new_vector
    
    def linear_combination(self,other: "Vector",scalar_self: float=1,scalar_other:float=1):
        linear_comb=np.add(self.vector*scalar_self,other.vector*scalar_other)
        return linear_comb
    
    def normalize(self):
        normalized_vector=self.vector/np.linalg.norm(self.vector)
        return normalized_vector




class Matrix():
    def __init__(self):
        pass
    
    def __str__(self):
        return f""
    
if __name__=="__main__":
    A = Vector([[4],[0],[3]])
    B = Vector([[1],[-2],[-3]])
    A.vector_contructor()
    B.vector_contructor()
    print(A)
    print(B)
    print(B.scalar_multiplication(10))
    print(Vector.linear_combination(A,B,1,-4))
    print(A.transpose())
    print(A.get_lenght())
    print(B.normalize())
