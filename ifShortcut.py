
nb=input("enter an int: ")
nb=int(nb)

if nb < 0:
    nbabs = -nb
else:
    nbabs = nb
print(nb, nbabs)

nbabs= -nb if nb < 0 else nb 
print(nb, nbabs)