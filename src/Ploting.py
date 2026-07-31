import matplotlib.pyplot as plt

def Create_Complex() -> list[int]:
    
    x_list : list[int] = []
    y_list : list[int] = []

    x= Input("Enter the real number = ")
    y = Input("Enter the inamginary number = ")

    complex_number = complex(x,y)

    x_list.append(x)
    y_list.append(y)
    
    while True:
        AskQuestion = Input("What do you want\n1 Scaling\n2 Degree Rotaion\n= ")
        
        if AskQuestion == 1:
            x1,y1 =Scaling(complex_number)
            break
        elif AskQuestion == 2:
            x1,y1 =RoationDegree(complex_number)
            break
        else:
            print("Plaese Enter the correct option")
            True
            
    x_list.append(x1)
    y_list.append(y1)
    
    return x_list,y_list

def Scaling(complex_number : complex) -> int:
    
    scale = [1/2,2,1/3]
    
    while True:
        ScaleValue= Input("Scaling number\n1 for half\n2 for Double\n3 for one Third(1/3)\n= ")
        
        match(ScaleValue):
            case 1:
                value = 0
                break
            case 2:
                value = 1
                break
            case 3:
                value = 2
                break
            case _ :
                print("please select the correct value")
                True
    
    Scale_complex_number : complex= complex_number * scale[value]
    print(Scale_complex_number)
    
    return Scale_complex_number.real,Scale_complex_number.imag
    
def RoationDegree(complex_number:complex) -> int:
    
    mul = [1,1j,-1,-1j]
    
    while True:
        degre_input = Input("Enter the degree = ")
    
        match(degre_input):
            case 0:
                degre = 0
                break
            case 90:
                degre = 1
                break
            case 180:
                degre = 2
                break
            case 270:
                degre=3
                break
            case _ :
                print("please enter correct coorderent")
                True
                

    Rotation_complex_number :complex = complex_number*mul[degre]
    print(Rotation_complex_number)
    
    return Rotation_complex_number.real,Rotation_complex_number.imag
    
def Create_Graph(x:int,y:int) :
        
    plt.plot(x, y, color='blue', linestyle='--', marker='o')
    plt.title("Simple Line Plot")
    plt.xlabel("X Axis Label")
    plt.ylabel("Y Axis Label")

    # Render to screen
    plt.show()
 
def Input(text:str)-> int:
    while True:
        try:
            inputvlaue = int(input(text))
            if inputvlaue < 0:
                raise ValueError
            break
        except ValueError:
            print("please enter valide value")
            True
    
    return inputvlaue
