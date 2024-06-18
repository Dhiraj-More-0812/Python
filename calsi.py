#from functions import *
from functions import add,substract
c=0
while(repeat>0):
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
    c=substract(a,b)
elif(choice==3):
    c=multiply(a,b)
elif(choice==4):
    c=divide(a,b)
else:
    print("invalid choice")
print("the result is",c)
repeat=int(input("press 6 to repeat or 7 to exit"))
