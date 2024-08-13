
#BasicCalculatorOperationsInPython


def main():
    while True:
        try:
            first_input = input("Enter first number (or press Enter to exit): ")
            if first_input == '':
                print("Exit.")
                break
            input_1 = int(first_input)  
            input_2 = int(input("Enter second number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            if operation == '+':
                print("Output: {}".format(add(input_1, input_2)))
            elif operation == '-':
                print("Output: {}".format(sub(input_1, input_2)))
            elif operation == '*':
                print("Output: {}".format(multi(input_1, input_2)))
            elif operation == '/':
                print("Output: {}".format(div(input_1, input_2)))
            else:
                print("Error: Invalid operation")
        
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")




def add(input_1, input_2):
    return input_1 + input_2

def sub(input_1, input_2):
    return input_1 - input_2

def multi(input_1, input_2):
    return input_1 * input_2

def div(input_1, input_2):
    if input_2 != 0:
        return input_1 / input_2
    else:
        return "Error: Division by zero"

main()