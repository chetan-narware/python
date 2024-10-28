import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#easy

passw= ""

no_letters=int(input("enter the number of letters u want in your password:"))
no_num=int(input("enter the number of numbers u want in your password:"))
no_symbols=int(input("enetr the number of symbols u want in your password:"))

for x in range(1,no_letters+1):
    char=random.choice(letters)
    passw=passw+char

for x in range(1,no_num+1):
    char=random.choice(numbers)
    passw=passw+char

for x in range(1,no_symbols+1):
    char=random.choice(symbols)
    passw=passw+char
print("easy")
print(passw)

#hard

pas=[]
for x in range(1,no_letters+1):
    char=random.choice(letters)
    pas.append(char)

for x in range(1,no_num+1):
    char=random.choice(numbers)
    pas.append(char)

for x in range(1,no_symbols+1):
    char=random.choice(symbols)
    pas.append(char)
myorder=[3,2,1,4,5,6,8,7]
a=int(input("enter what 0 for suffle and 1 for forloop randomization"))
if a==0:
    random.shuffle(pas)
else:
    pas=[pas[i] for i in myorder]

print(pas)



