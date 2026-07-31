from src.Ploting import Input

def Create_vector(n) -> list[int]:
    vector_list : list[int] = []
    for i in range(n):
        x = Input(f"enter the {i+1} vector value = ")
        vector_list.append(x)
    
    return vector_list

def Sum_vector(vector_u : list[int] , vector_v :list[int]) -> list[int]:
        
    sum_list = list(map(lambda x ,y : x + y , vector_u,vector_v))
        
    return sum_list

def Scaler_multiplication(Scalar : int, vector_list : list[int] ) -> list[int]:
    
    Scaler_mul_list = list(map(lambda x : x * Scalar , vector_list))
    return Scaler_mul_list

def Vector_multiplication(vector_u :list[int] , vector_v : list[int]) -> int:
    Vector_mul_list = list(map(lambda x,y : x*y , vector_u , vector_v))
    sums = 0
    for i in Vector_mul_list:
        sums +=i
    
    return  sums

def main_func():
    Vector_length : int = Input("Please enter the length of vector = ")
    
    vector_u : list[int] = Create_vector(Vector_length)
    print(f"vector U = {vector_u}")
    
    vector_v: list[int] = Create_vector(Vector_length)
    print(f'vector v = {vector_v}')

    
    while True:
        AskQuestion = Input('\nwhat do you want\n1 vector au + bv\n2 Dot product of u & v \nif exit 0\n= ')
        
        if AskQuestion== 1 :
            Sacler_a : int = Input("Enter the Scaler a = ")
            
            Sacler_b  : int= Input("Enter the Scaler b = ")
            
            multiply_ua : list[int]= Scaler_multiplication(Sacler_a,vector_u)
            multiply_vb : list[int] = Scaler_multiplication(Sacler_b,vector_v)
            
            Answer:list[int] = Sum_vector(multiply_ua,multiply_vb)
            print(f' ua + vb = {Answer}')
        
        elif AskQuestion == 2 : 
            mutiply_uv : int = Vector_multiplication(vector_u,vector_v)
            print(f'Dot Product of vectot u and v = {mutiply_uv}')
        elif AskQuestion == 0 :
            print('thank you')
            break
        else:
            print('please enter valide number')
            True