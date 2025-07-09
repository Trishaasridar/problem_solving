p=int(input()) # get liter of paint
b=int(input()) # get no of badges
d=int(input()) # get amount of per badge

rem= (p % b) # assinging the rem liter of paint
print((int(p/b) * d ) + rem) # printing the no of pokedollars