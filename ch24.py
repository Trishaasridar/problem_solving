opended_suitcase=int(input()) # no of opended suitcases
amount=[100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
list_suit=[] # get the indexes append

for suitcase in range(opended_suitcase):
    suit=int(input())
    list_suit.append(suit-1) # append the index with -1
    
for i in sorted(list_suit,reverse=True): # sort desendingly
    amount.pop(i)  # pop out the amount

bank_offer=int(input()) # get the amount offered by bank

average=sum(amount)/len(amount) # calculate avg

if bank_offer>average: # if bank offer is larger
    print("deal") # print deal
else : 
    print("no deal") # print no deal

    