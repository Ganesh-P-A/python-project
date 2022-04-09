def add(a,b): #calculator functions
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mul(a,b):
    return(a*b)

def task(): #core of calculator
    while True:
        m="please enter operation as +,-,*,/"
        print(m.center(67," ")) #centers 'm ' string
        z=input("enter what operation you want to do ")       
 
        if "thank you" in z: #to get out from loop
            import sys
            sys.exit() 

        a=int(input("enter first number "))        
        b=int(input("enter second number "))

        if "+"==z:
            print("      addition is",add(a,b))
            
        elif "-"==z:
            print("    subtraction is",sub(a,b))
            
        elif "*"==z:
            print("   multiplication is",mul(a,b))
            
        elif "/"==z:
            print("   division is",div(a,b))
            
        else:
            print("   invalid operation selected")
            
task()