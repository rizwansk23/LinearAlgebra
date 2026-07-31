from .Ploting import Input

def Operation():
    
    complex_1 = Create_complex_number()
    complex_2 = Create_complex_number()
    
    while True:
        AskQuestion = Input("\n1: Addition\n2: Substraction\n3: Mutiplication\n4: Conjugate\nif exit 0\n= ")
        
        match(AskQuestion):
            case 0:
                print("Thank you")
                break
            case 1:
                
                # ifcomplex_2 = Ifexistong()
                # if ifcomplex_2 is not None:
                #     Addition(complex_1,ifcomplex_2)
                    
                Addition(complex_1,complex_2) 
            case 2:
                Substraction(complex_1,complex_2)
            case 3:
                Multiplication(complex_1,complex_2)
            case 4:
                Conjugate(complex_1,complex_2)
            case _:
                print(" choose valid input")
    


def Create_complex_number():
    
    x:int = Input("Enter the Real Number = ")
    y : int = Input("Enter the Imaginary Number = ")
    
    complex_number : complex = complex(x,y)
    
    return complex_number

def Addition(complex_1:complex,complex_2:complex):
    print(f"Additon of {complex_1} + {complex_2} = {complex_1+complex_2}")
    
def Substraction(complex_1:complex,complex_2:complex):
    print(f"Substraction of {complex_1} - {complex_2} = {complex_1-complex_2}")

def Multiplication(complex_1:complex,complex_2:complex):
    print(f"Multiplication of {complex_1} * {complex_2} = {complex_1*complex_2}")

    
def Conjugate(complex_1:complex,complex_2:complex):
    z1 = complex_1.conjugate()
    z2 = complex_2.conjugate()
    
    print(f"Conjugate of {complex_1} = {z1}")
    print(f"Conjugate of {complex_2} = {z2}")

def Ifexistong() -> complex | None:
    
    while True:
        
        askQuestion = Input("1:if new complex number\n2:go to existing\n= ")
        
        match(askQuestion):
            case 1:
                complex_2 = Create_complex_number()
            case 2:
                return None
            case _ :
                print("please enter valide number")
                break
    
        return complex_2
                

  