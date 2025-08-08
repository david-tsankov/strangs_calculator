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
    
    def dot_product(self,other: "Vector",self_scalar:float=1,other_scalar:float=1):
        """Input must be two vectors of the same shape, as function takes care of transposition and shape alignment."""
        self.vector=np.transpose(self.vector)
        dot_product=np.dot(self.vector*self_scalar,other.vector*other_scalar)
        return dot_product
    
    def cross_product(self, other: "Vector"):
        """The function takes only vertical vectors with 3 components (3D), """
        if self.vector.shape[0]==3 and other.vector.shape[0]==3:
            self.vector=np.transpose(self.vector)
            other.vector=np.transpose(other.vector)
            cross_product=np.cross(self.vector,other.vector)
            return np.transpose(cross_product)
        else: 
            return f"Either vectors aren't vertical, or vectors aren't 3D, if you wish to use 2D vectors, append a [0] as a third component on each vector!"
        
        
        
    
if __name__=="__main__":
    A = Vector([[4],[0],[3]])
    B = Vector([[1],[-2],[-3]])
    A.vector_contructor()
    B.vector_contructor()
    print(A)
    print(B)
    # print(B.scalar_multiplication(10))
    # print(Vector.linear_combination(A,B,1,-4))
    # A_trans=A.transpose()
    # print(A.transpose())
    # print(A.get_lenght())
    # print(B.normalize())
    # print(Vector.dot_product(A,B))
    print(Vector.cross_product(A,B))