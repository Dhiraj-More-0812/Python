#from calcy import*
from  calcy import add,subtract
c=0
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

if(choice<5):
    
    print("The result is: ",c)

