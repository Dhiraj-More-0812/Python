import calcy
c=0
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("1:Addition")
print("2:Subtraction")
print("3:Multiplication")
print("4:Division")
choice=int(input("Enter your choice: "))
if (choice==1):
    c=calcy.add(a,b)
elif(choice==2):
    c=calcy.subtract(a,b)
elif(choice==3):
    c=calcy.multiplication(a,b)
elif(choice==4):
    c=calcy.divide(a,b)
else:
    print("Invalid choice.")

if(choice<5):
    
    print("The result is: ",c)


