def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)
no1=eval(input("Enter the first number--> "))
no2=eval(input("Enter the second number--> "))
print("select the option:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
while True:
    choice=int(input("Enter your choice: "))
    if choice in (1,2,3,4,5):
        if choice==1:
            print("addition of two numbers is:",add(no1,no2))
        elif choice==2:
            print("subtraction of two numbers is:",subtract(no1,no2))
        elif choice==3:
            print("multiplication of two numbers is:",multiply(no1,no2))
        elif choice==4:
            print("division of two numbers is:",divide(no1,no2))
        elif choice==5:
            print("Thank you for using calculator")
            exit()
        else:
            print("Invalid choice")