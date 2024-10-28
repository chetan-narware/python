import art
print(art.gavel)
import os
bids={}
conti=True
while conti:
    name=input("please enter your name:\n")
    bid=int(input("please enter your bid in $:\n"))
    cont=input("are there other bids?:yes/no\n")

    bids[name]=bid
     
    if cont=="no":
        conti=False
    else:
        os.system('cls')

max=0
for key in bids:
    if bids[key]>max:
        max_key=key
        max=bids[key]

print(f"auction is won by {max_key} for {max}$")