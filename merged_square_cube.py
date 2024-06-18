def square(num):
    s=num*num
    print("Square of the number is: ",s)
    return(s)

def cube(num):
    c=num*num*num
    print("The cube of the number is: ",c)

num=int(input("Enter a number:"))
cube(square(num))
