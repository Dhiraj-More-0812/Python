Math=int(input("Enter math marks: ")) # math marks obtained by the student
Science=int(input("Enter science marks: ")) #science marks obtained by the student
English=int(input("Enter english marks: ")) # english marks obtained by the student
fop=int(input("Enter fop marks: "))# fop marks obtained by the student
total=Math+Science+English+fop # total of the marks
percentage=total/100*100 # percentage of the student
print("Percentage: ",percentage,"%")
if (percentage>=75):
    print("You have got distinction!")
elif (percentage>=60 and percentage<75):
    print("You have got first class!")
elif (percentage>=50 and percentage<60):
    print("You have got second class!")
elif (percentage>=40 and percentage<50):
    print("You have got third class!")
else :
    print("Sorry! You have failed.")
