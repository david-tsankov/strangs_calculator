#functions 
import numpy as np

def dot_product():
    pass

def cross_product():
    pass

def get_lenght():
    pass

def construct_vector():
    def user_input():
        vector_name = input("Give a symbol to represent the vector (e.g. A): ")
        return vector_name
    vector_name=user_input()
    vector_name=np.array(input("Enter vector by documentations' syntax: "))
    return vector_name

def construct_matrix():
    def user_input():
        matrix_name = input("Give a symbol to represent the matrix (e.g. A): ")
        return matrix_name
    matrix_name=user_input()
    matrix_name=np.array(input("Enter matrix by documentations' syntax: "))
    return matrix_name

def get_inverse():
    pass

def get_determinant():
    pass

def check_singularity():
    pass

def get_column_space():
    pass

def get_basis_for_column_space():
    pass

def get_nullspace():
    pass

def get_elimination_matrix():
    pass

def get_eigenvalues():
    pass

def get_eigenvectors():
    pass

def get_cayley_hamilton_equation():
    pass

def linear_combination_vectors():
    pass

def solve_system_of_equations():
    pass

def matrix_multiplication():
    pass

def transpose(matrix: np.array):
    np.transpose(matrix)
    return matrix


if __name__ == "__main__":
    print(construct_matrix())
