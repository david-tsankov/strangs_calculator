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
    
    def linear_combination(self, other: "Vector"):
        linear_comb=np.add(self.vector,other.vector)
        return linear_comb
    
    def scalar_multiplication(self, scalar: float=1):
        new_vector=np.dot(self.vector, scalar)
        return new_vector



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
    print(Vector.linear_combination(A,B))
    print(A.transpose())
    print(A.get_lenght())
