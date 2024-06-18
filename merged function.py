def square(num):
    s=num*num
    print("the square of the number is:",s)
    return(s)
    
def cube(num):
    s=num*num*num
    print("the cube of the number is:",s)

num=int(input("enter the number:"))
cube(square(num))

