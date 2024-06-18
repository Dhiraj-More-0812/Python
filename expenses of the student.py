#total expenses of a student in a month
f=int(input("Enter monthly fees: ")) #monthly fees of the student
t=int(input("Enter travelling expenses: ")) # travelling expenses of the student
b=int(input("Enter book charges: ")) #charges of books of the student
p=int(input("Enter project/activity charges: ")) #project and activity charges of the student
TE=f+t+b+p #total monthly expenses of the student
print("Total monthly expenses of the student: ",TE,"Rs")
#total expenses of a student in a year
YE=TE*12 #Yearly expenses of the student
print("Yearly expenses of the student: ",YE,"Rs")
#total expenses of the student throughout Diploma
DE=YE*3 #Diploma expenses of the student
print("Diploma expenses of the student: ",DE,"Rs")
