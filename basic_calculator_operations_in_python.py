#Basic Calculator Operations in Python

def add(input_1,input_2):
    return input_1+input_2

def sub(input_1,input_2):
    return input_1+input_2

def multi(input_1,input_2):
    return input_1+input_2

def div(input_1,input_2):
    return input_1+input_2

input_1=int(input("Enter first number="))
input_2=int(input("Enter second number="))
operation=input("Enter the operation(+,-,*,/)=")


if operation=='+':
    print("Output={}".format(add(input_1,input_2)))
elif operation=='-':
    print("Output={}".format(sub(input_1,input_2)))
elif operation=='*':
    print("Output={}".format(multi(input_1,input_2)))
elif operation=='/':
    print("Output={}".format(div(input_1,input_2)))
else:
    print("Invalid input")