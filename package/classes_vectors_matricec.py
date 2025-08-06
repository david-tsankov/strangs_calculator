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



class Matrix():
    def __init__(self):
        pass
    
    def __str__(self):
        return f""
    
if __name__=="__main__":
    A = Vector([[4],[0],[3]])
    A.vector_contructor()
    print(A)
    print(A.transpose())
    print(A.get_lenght())
