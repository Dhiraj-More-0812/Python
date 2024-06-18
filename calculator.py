def add(a,b):
    c=a+b
    return(c)

def subtract(a,b):
    c=a-b
    return(c)

def multiplication(a,b):
    c=a*b
    return(c)

def divide(a,b):
    c=a/b
    return(c)

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

print("1:Addition")
print("2:Subtraction")
print("3:Multiplication")
print("4:Division")
choice=int(input("Enter your choice: "))
if (choice==1):
    c=add(a,b)
elif(choice==2):
    c=subtract(a,b)
elif(choice==3):
    c=multiplication(a,b)
elif(choice==4):
    c=divide(a,b)
else:
    print("Invalid choice.")
    
print("The result is: ",c)


