import numpy as np
from linear_modules.class_matrices import Matrix
from linear_modules.class_vectors import Vector
from linear_modules.matrix_and_vector_functions import solve_system_of_equations

print(f"{"Welcome to Strangs Calculator":^100}")
print(f"{100*"-"}")
print(f"{"Keep in mind to perform any operation you must first construct a vector/matrix!":^100}")
print(f"{100*"-"}")
print(f"{"1 ---> Construct a vector":^50}{"2 ---> Construct a matrix":^50}")
print("\n")
print(f"{"3 ---> Vector operations":^33.33}{"4 ---> Matrix operations":^33.33}{"5 ---> Other operations":^33.33}")
print(f"{100*"-"}")
print("\n")

def operation_input():
    def syntax_editor():    
        _=numbers
        _=_.split(",")
        components=[]
        for component in _:
            print(type(component))
            component=int(component)
            print(type(component))
            components.append([int(component)])

        return components
    
    operation=int(input("Enter operation class: "))

    if operation==1:
        vector=input("Enter a variable to represent the vector (x,b,v): ")
        numbers=input("Enter the vector components, separated by a coma: ")
        vector=Vector(syntax_editor())
        vector.vector_construct()
        print(vector)
        
    elif operation==2:
        print("Youre constructing a matrix")
    elif operation==3:
        print("Vector operations")
    elif operation==4:
        print("Matrix operations")
    elif operation==5:
        print("Other operations")
    else:
        print("Please enter a valid entry!")
        operation_input()
    
operation_input()





# Draft for the function using hard coded components

def syntax_editor():    
    _=numbers
    _=_.split(",")
    components=[]
    for component in _:
        print(type(component))
        component=int(component)
        print(type(component))
        components.append([int(component)])

    return components
# print(syntax_editor())