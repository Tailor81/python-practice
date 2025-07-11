action = input("enter your operation ")
num1 = int(input("please enter number 1 "))
num2 = int(input("please enter number 2"))


def addition(num1, num2):
    addition = num1 + num2

    return addition

def subtraction(num1, num2):
    sub = num1 - num2

    return sub

def multiply(num1, num2):
    multiply = num1 * num2
    
    return multiply

def division(num1, num2):
    division = num1 / num2

    return division



def calculator():
    if action == "adition":
        return addition(num1, num2)
    
    elif action == "multiplecation":
        return multiply(num1, num2)
    
    
    elif action == "subtraction":
        return subtraction(num1, num2)
    
    
    elif action == "division":
        return division(num1, num2)
    
    
print(calculator())

    

    
