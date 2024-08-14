#PythonPrintFunctionsPracticeQuestions

#1. Basic Printing
print("Hello,World!")
print("Afia")
print("\n")

#2. Printing Multiple Items
print("Afia","Mushtaq")
print(1,2,3)
print("\n")

#3. Printing Special Characters
print("Hello\nWorld")
print("Hello\tWorld")
print("\n")

#4. Using the sep Parameter
print("apple","banana","cherry",sep=",")
print(1,2,3,sep="-")
print("\n")

#5. Using the end Parameter
print("Hello",end=" ")
print("World")
print(1,end="")
print(2)
print("\n")

#6. Escape Characters
print('He said,"Hello"')
print("This is a backslash:\.")
print("\n")

#7. Combining Text and Numbers
age=25
print("I am {} years old.".format(age))
num=1
print("The number is {}".format(num))
print("\n")

#8. Basic Loop for Printing
for i in range(1,6):
    print(i)