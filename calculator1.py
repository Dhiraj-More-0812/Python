
def add(a,b):C=0
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("1: add")
print("2: subtraction")
print("3: multiply")
print("4: divide")
choice=int(input("enter your choice:"))
if(choice==1):
    c=add(a,b)
elif(choice==2):
    c=substraction(a,b)
elif(choice==3):
    c=multiply(a,b)
elif(choice==4):
    c=divide(a,b)
else:
    print("invalid choice")
print("the result is",c)

