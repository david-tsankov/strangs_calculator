import numpy as np

# class Vector:
#     def __init__(self, components, name):
#         self.components = components
#         self.name = name

#     def vector_construct(self):
#         self.components=np.array(self.components)

#     def __str__(self):
#         return f"{self.name} =\n{self.components}"
    
#     def get_lenght(self):
#         norm=np.linalg.norm(self.components)
#         return norm
    
#     def transpose(self):
#         vector_transpose=np.transpose(self.components)
#         return vector_transpose
    
#     def scalar_multiplication(self, scalar: float=1):
#         new_vector=np.dot(self.components, scalar)
#         return new_vector
    
#     def linear_combination(self,other: "Vector",scalar_self: float=1,scalar_other:float=1):
#         linear_comb=np.add(self.components*scalar_self,other.components*scalar_other)
#         return linear_comb
    
#     def normalize(self):
#         normalized_vector=self.components/np.linalg.norm(self.components)
#         return normalized_vector
    
    # def dot_product(self,other: "Vector",self_scalar:float=1,other_scalar:float=1):
    #     """Input must be two vectors of the same shape, as function takes care of transposition and shape alignment."""
    #     self.components=np.transpose(self.components)
    #     dot_product=np.dot(self.components*self_scalar,other.components*other_scalar)
    #     return dot_product
    
    # def cross_product(self,self.name other: "Vector"):
    #     """The function takes only vertical vectors with 3 components (3D), """
    #     if self.components.shape[0]==3 and other.components.shape[0]==3:
    #         self.components=np.transpose(self.components)
    #         other.components=np.transpose(other.components)
    #         cross_product=np.cross(self.components,other.components)
    #         return np.transpose(cross_product)
    #     else: 
    #         return "Either vectors aren't vertical, or vectors aren't 3D, if you wish to use 2D vectors, append a [0] as a third component on each vector!"
        
class Vector_Manager():
    vector_objects={

    }
    def __init__(self, components, name):
        self.components=components
        self.name=name

    def object_saver(self):
        Vector_Manager.vector_objects[self.name]=self

    def dot_product(self,other: "Vector_Manager",self_scalar:float=1,other_scalar:float=1):
        """Input must be two vectors of the same shape, as function takes care of transposition and shape alignment."""
        self.components=np.transpose(self.components)
        dot_product=np.dot(self.components*self_scalar,other.components*other_scalar)
        return dot_product
    
    def cross_product(self, other: "Vector_Manager"):
        """The function takes only vertical vectors with 3 components (3D), """
        if self.components.shape[0]==3 and other.components.shape[0]==3:
            self.components=np.transpose(self.components)
            other.components=np.transpose(other.components)
            cross_product=np.cross(self.components,other.components)
            return np.transpose(cross_product)
        else: 
            return "Either vectors aren't vertical, or vectors aren't 3D, if you wish to use 2D vectors, append a [0] as a third component on each vector!"
    
    def linear_combination(self,other: "Vector_Manager",scalar_self: float=1,scalar_other:float=1,name_comb: str="Combination"):
        linear_comb=np.add(self.components*scalar_self,other.components*scalar_other)
        comb_object=Vector_Manager(linear_comb, name_comb)
        Vector_Manager.object_saver(comb_object)
        return comb_object
    
    def list_vectors():
        for name, object in Vector_Manager.vector_objects.items():
            print(f"{object}")
        return ""

    ###
    def vector_construct(self):
        self.components=np.array(self.components)

    def __str__(self):
        return f"{self.name} =\n{self.components}"
    
    def get_lenght(self):
        norm=np.linalg.norm(self.components)
        return norm
    
    def transpose(self):
        self.components=np.transpose(self.components)
        Vector_Manager.object_saver(self)
        return self.components
    
    def scalar_multiplication(self, scalar: float=1):
        self.components=np.dot(self.components, scalar)
        Vector_Manager.object_saver(self)
        return self.components
    
    def normalize(self):
        self.components=self.components/np.linalg.norm(self.components)
        Vector_Manager.object_saver(self)
        return self.components
        
        
        

        
    
if __name__=="__main__":

    x=Vector_Manager([[1],[0],[0]],"x")
    Vector_Manager.vector_construct(x)
    Vector_Manager.object_saver(x)
    B=Vector_Manager([[2],[-1],[5]],"B")
    Vector_Manager.vector_construct(B)
    Vector_Manager.object_saver(B)
    print(Vector_Manager.vector_objects)
    Vector_Manager.list_vectors()
    lin_comb=Vector_Manager.linear_combination(x,B,1,1,"C")
    print(lin_comb)
    