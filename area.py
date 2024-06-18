lh=int(input(" Enter Length of the hall: ")) #length of hall
wh=int(input("Enter Width of the hall: ")) #width of hall
lt=int(input("Enter Length of the tile: ")) #length of tile
wt=int(input("Enter Width of the tile: ")) #width of tile
ah=lh*wh #area of hall
at=lt*wt #area of tile
nt=ah/at #number of tiles required
print("Total number of tiles required=",nt,"tiles.")
