number1=int(input("Enter The First Number:"))
number2=int(input("Enter The Second Number:"))
def Addition(number1,number2):
    return number1+number2
def Substraction(number1,number2):
    return number1-number2
def Multiplication(number1,number2):
    return number1*number2
def Division(number1,number2):
    return number1/number2
print("Enter your choice \n 1.Addition \n 2. Substraction \n 3. Multiplication \n 4.Division")
choice=int(input())
if choice == 1:
    print("Addition Of Two Numbers is",Addition(number1,number2))
elif choice == 2:
    print("Substraction Of Two Numbers is ",Substraction(number1,number2))
elif choice == 3:
    print("Multiplication Of Two Numbers is",Multiplication(number1,number2))
elif choice == 4:
    print("Division Of Two Numbers is",Division(number1,number2))
