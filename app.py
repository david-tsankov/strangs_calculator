# TODO: Break the big functioin into smaller functions

from linear_modules.class_matrices import Matrix
from linear_modules.class_vectors import Vector_Manager
def main_menu():
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

def vector_menu():
    print(f"{100*"-"}")
    print(f"{"Vector operations: ":^100}")
    print(f"{100*"-"}")
    print(f"{"1 ---> List all vectors":^33.33}{"2 ---> Get lenght":^33.33}{"3 ---> Transpose":^33.33}")
    print("\n")
    print(f"{"4 ---> Scalar multiplication":^33.33}{"5 ---> Linear combination":^33.33}{"6 ---> Normalize":^33.33}")
    print("\n")
    print(f"{"7 ---> Dot product":^33.33}{"8 ---> Cross product":^33.33}{"9 ---> Back to main menu":^33.33}")
    print(f"{100*"-"}")

def syntax_editor_vector(components):    
    components=components.split(",")
    numpy_array=[]
    for component in components:
        component=int(component)
        numpy_array.append([int(component)])

    return numpy_array

def operation_input():
    operation=int(input("Enter operation class: "))

    if operation==1:
        name=input("Enter a variable to represent the vector (x,b,v): ")
        components=input("Enter the vector components, separated by a coma: ")
        components=syntax_editor_vector(components)
        vector_object=Vector_Manager(components,name)
        Vector_Manager.vector_construct(vector_object)
        Vector_Manager.object_saver(vector_object)
        print(f"Succesfully created vector: {vector_object}")
        operation_input()

    elif operation==2:
        matrix_name=input("Enter a variable to represent the matrix (A,E,M): ")
        matrix_components=input("Enter the matrix components, separating the rows by a $,\nand the components of each row by a ',' e.g.(1,2,3$4,5,6$7,8,9): ")
        # matrix_name=Matrix(syntax_editor_matrix(matrix_components),matrix_name)
        matrix_name.matrix_construct()
        print("Succesfully created matrix, matrix list: ")
        Matrix.matrix_list()
        operation_input()

    elif operation==3:
        vector_menu()
        def operation_3():
            vector_operation=int(input("Enter vector operation: "))

            if vector_operation==1:
                Vector_Manager.list_vectors()
                operation_3()

            if vector_operation==2:
                try:
                    name=input("Enter the variable representing the vector (x,b,v): ")
                    vector_object=Vector_Manager.vector_objects[name]
                    print(f"Lenght = {Vector_Manager.get_lenght(vector_object)}")
                except Exception:
                    print("Please enter a valid variable")
                operation_3()

            if vector_operation==3:
                try:
                    name=input("Enter the variable representing the vector (x,b,v): ")
                    vector_object=Vector_Manager.vector_objects[name]
                    vector_object=Vector_Manager.transpose(vector_object)
                    print(f"Transposed vector -->\n {vector_object}")
                    operation_3()
                except Exception:
                    print("Please enter a valid variable")

            if vector_operation==4:
                try:
                    name=input("Enter the variable representing the vector (x,b,v): ")
                    vector_object=Vector_Manager.vector_objects[name]
                    scalar=float(input("Please enter a scalar multiplier: "))
                    vector_object=Vector_Manager.scalar_multiplication(vector_object, scalar)
                    print(f"Scaled vector -->\n {vector_object}")
                    operation_3()
                except Exception:
                    print("Please enter a valid variable")

            if vector_operation==5:
                try:
                    name1=input("Enter the variable representing the first vector (x,b,v): ")
                    scalar1=float(input("Enter the first scalar multiplier: "))
                    name2=input("Enter the variable representing the second vector (x,b,v): ")
                    scalar2=float(input("Enter the second scalar multiplier: "))
                    name_comb=input("Enter a variable(s) to represent the combination: ")
                    vector_object1=Vector_Manager.vector_objects[name1]
                    vector_object2=Vector_Manager.vector_objects[name2]
                    linear_combination=Vector_Manager.linear_combination(vector_object1, vector_object2, scalar1, scalar2, name_comb)
                    print(f"Linear combination -->\n {linear_combination}")
                    operation_3()
                except Exception:
                    print("Please enter valid variables/scalars: ")

            if vector_operation==6:
                try:
                    name=input("Enter the variable representing the vector (x,b,v): ")
                    vector_object=Vector_Manager.vector_objects[name]
                    vector_object=Vector_Manager.normalize(vector_object)
                    print(f"Normalized vector =\n{vector_object}")
                    operation_3()
                except Exception:
                    print("Please enter a valid variable: ")

            if vector_operation==7:
                try:
                    name1=input("Enter the variable representing the first vector (x,b,v): ")
                    name2=input("Enter the variable representing the second vector (x,b,v): ")
                    vector_object1=Vector_Manager.vector_objects[name1]
                    vector_object2=Vector_Manager.vector_objects[name2]
                    dot_product=Vector_Manager.dot_product(vector_object1, vector_object2)
                    print(f"{dot_product}")
                    operation_3()
                except Exception:
                    print("Please enter valid variables: ")

            if vector_operation==8:
                try:
                    name1=input("Enter the variable representing the first vector (x,b,v): ")
                    name2=input("Enter the variable representing the second vector (x,b,v): ")
                    name_cross=input("Enter a variable representing the cross product: ")
                    vector_object1=Vector_Manager.vector_objects[name1]
                    vector_object2=Vector_Manager.vector_objects[name2]
                    cross_product=Vector_Manager.cross_product(vector_object1, vector_object2, name_cross)
                    print(f"Cross product = {cross_product}")
                    operation_3()
                except Exception:
                    pass

            if vector_operation==9:
                try:
                    main_menu()
                    operation_input()
                except Exception:
                    print("Please enter a valid vector operation: ")

        operation_3()


    elif operation==4:
        print("Matrix operations")
    elif operation==5:
        print("Other operations")
        Vector_Manager.list_vectors()
        operation_input()
    elif operation==6:
        print("Thanks for using Strangs calculator")
    else:
        print("Please enter a valid entry!")
        operation_input()

main_menu() 
operation_input()


    

    # def syntax_editor_matrix(matrix_components):
    #     numbers=[]
    #     matrix_components=matrix_components.split("$")
    #     print(matrix_components)
    #     for row in matrix_components:
    #         row=row.split(",")
    #         index=0
    #         for ij in row:
    #             row[index]=int(ij)
    #             index+=1
    #         numbers.append(row)
    #     return numbers
