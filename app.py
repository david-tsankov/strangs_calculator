# TODO: Write function to list all instances of each class, e.g. you create a vector x with components 1,2,3 output: x: [[1],[2],[3]]
# so people can track what vectors theyve created 

from linear_modules.class_matrices import Matrix
from linear_modules.class_vectors import Vector
from linear_modules.matrix_and_vector_functions import solve_system_of_equations

print(f"{"Welcome to Strangs Calculator":^100}")
print(f"{100*"-"}")
print(f"{"Keep in mind to perform any operation you must first construct a vector/matrix!":^100}")
print(f"{100*"-"}")
print(f"{"1 ---> Construct a vector":^50}{"2 ---> Construct a matrix":^50}")
print("\n")
print(f"{"3 ---> Vector operations":^50}{"4 ---> Matrix operations":^50}")
print("\n")
print(f"{"5 ---> Other operations":^50}{"6 ---> Exit":^50}")
print(f"{100*"-"}")
print("\n")

def operation_input():
    def syntax_editor_vector():    
        _=numbers
        _=_.split(",")
        components=[]
        for component in _:
            component=int(component)
            components.append([int(component)])

        return components
    

    def syntax_editor_matrix(matrix_components):
        numbers=[]
        matrix_components=matrix_components.split("$")
        print(matrix_components)
        for row in matrix_components:
            row=row.split(",")
            index=0
            for ij in row:
                row[index]=int(ij)
                index+=1
            numbers.append(row)
        return numbers
    
    operation=int(input("Enter operation class: "))

    if operation==1:
        vector_name=input("Enter a variable to represent the vector (x,b,v): ")
        numbers=input("Enter the vector components, separated by a coma: ")
        vector_components=syntax_editor_vector()
        vector_name=Vector(vector_components,vector_name)
        vector_name.vector_construct()
        print("Succesfully created vector, vector list: ")
        Vector.vectors_list()
        operation_input()

    elif operation==2:
        matrix_name=input("Enter a variable to represent the matrix (A,E,M): ")
        matrix_components=input("Enter the matrix components, separating the rows by a $ and the components of each row by a , e.g.(1,2,3$4,5,6$7,8,9): ")
        matrix_name=Matrix(syntax_editor_matrix(matrix_components),matrix_name)
        matrix_name.matrix_construct()
        print("Succesfully created matrix, matrix list: ")
        Matrix.matrix_list()
        operation_input()
    elif operation==3:
        print("Vector operations")
    elif operation==4:
        print("Matrix operations")
    elif operation==5:
        print("Other operations")
    elif operation==6:
        print("Thanks for using Strangs calculator")
    else:
        print("Please enter a valid entry!")
        operation_input()
    
operation_input()





# Draft for the function using hard coded components

# def syntax_editor_vector():    
#     _=numbers
#     _=_.split(",")
#     components=[]
#     for component in _:
#         print(type(component))
#         component=int(component)
#         print(type(component))
#         components.append([int(component)])

#     return components
# print(syntax_editor_vector())

# Drafto for function for input of a matrix
# matrix_components="1,2,3$4,5,6$7,8,9"

# def syntax_editor_matrix():
#     numbers=[]
#     matrix_components="1,2,3$4,5,6$7,8,9"
#     matrix_components=matrix_components.split("$")
#     print(matrix_components)
#     for row in matrix_components:
#         row=row.split(",")
#         index=0
#         for ij in row:
#             row[index]=int(ij)
#             index+=1
#         numbers.append(row)
#     print(numbers)
    

# syntax_editor_matrix()