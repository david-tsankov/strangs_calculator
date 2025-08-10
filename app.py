# TODO: Break the big functioin into smaller functions

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
    operation=int(input("Enter operation class: "))
    
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
        matrix_components=input("Enter the matrix components, separating the rows by a $,\nand the components of each row by a ',' e.g.(1,2,3$4,5,6$7,8,9): ")
        matrix_name=Matrix(syntax_editor_matrix(matrix_components),matrix_name)
        matrix_name.matrix_construct()
        print("Succesfully created matrix, matrix list: ")
        Matrix.matrix_list()
        operation_input()

    elif operation==3:
        print(f"{100*"-"}")
        print(f"{"Vector operations: ":^100}")
        print(f"{100*"-"}")
        print(f"{"1 ---> List all vectors":^33.33}{"2 ---> Get lenght":^33.33}{"3 ---> Transpose":^33.33}")
        print("\n")
        print(f"{"4 ---> Scalar multiplication":^33.33}{"5 ---> Linear combination":^33.33}{"6 ---> Normalize":^33.33}")
        print("\n")
        print(f"{"7 ---> Dot product":^33.33}{"8 ---> Cross product":^33.33}{"9 ---> Back to main menu":^33.33}")
        print(f"{100*"-"}")
        def operation_3():
            vector_operation=int(input("Enter vector operation: "))

            if vector_operation==1:
                Vector.vectors_list()
                operation_3()

            if vector_operation==2:
                vector_for_lenght=input("Enter the variable representing the vector (x,b,e): ")
                vector_object=Vector.vector_objects[vector_for_lenght]
                print(f"Lenght = {vector_object.get_lenght()}")
        operation_3()


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

# Draft for function for input of a matrix
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