from src.Ploting import Input
from src.Vectors import Scaler_multiplication
from typing import List
import numpy as np


def Main():
    size : int = Input('Please Enter the Number of Row/Column')
    
    M : List[List[int]]= [[] for _ in range(0,size)]
    
    for i in range(0,size):
        for j in range(0,size):
            x = Input(f'please enter the {i + 1} by { j + 1 } = ')
            M[i].append(x)
    
    print(f'Matrix = {M}')
    while True:
        choice =Input("Please Choice Operation to Perform :\n1. Scaler Multiplication \n2.Transpose \n3.Fetch Rows and Column \n0.Exit\n =")
        if choice == 1:
            scaler_number=Input("Enter Number for Scaler Multiplication:")
            # Display Scaler Multiplication
            for i,m in enumerate(M):
                print(Scaler_multiplication(scaler_number,M[i]))
        elif choice == 2:
            Matrix=np.array(M)
            print("Transpose of matrix = ")
            print(Matrix.T)
            #Display Transpose of Matrix
        elif choice == 3:
            Fetch_Row_Column(matrix=M)
        elif choice == 0:
            print("Thank You")
            break
        else:
            print("Error")
            
        
def Fetch_Row_Column (matrix):
    while True:
        AsqQuestion = Input("What do you want o print ?\n1. Row\n2. Column\n3.Exit =")
        types = 'not valid'
        match (AsqQuestion):
            case 1:
                types = 'Row'
            case 2:
                types = "Column"
            case 0 :
                break
            case _ :
                True    
        DisplayMatrix(type=types,matrix=matrix)
    
        # if braek than break otherwise remove break keyword
      
    
def DisplayMatrix(type : str, matrix : List[List[int]]):
    if type == 'Row':
        for i , m in enumerate(matrix,start=1):
            print(f'Row {i}  = {m}')
    elif type == "Column":
        for i in range(len(matrix)):
            column = []
            for j in range(len(matrix)):
                column.append(matrix[j][i])
            print(f'column {i+1} = {column}')
    else:
        print('Please Enter correct option')
        