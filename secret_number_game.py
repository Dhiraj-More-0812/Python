N=9
C=0
L=3
while(C<L):
    guess=int(input("Guess: "))
    C+=1
    if guess==N:
        print('You won!')
        break
else:
    print('Sorry! You failed.')
