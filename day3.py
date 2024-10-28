print("welcome to the roller coaster")
h=int(input("enter the height in cm:\t"))
a=int(input("enetr ur age:"))
bill=0
if h>120:
    if a>=18:
        print("pay 18$")
        bill=18
    elif 12<=a<18:
        print("pay 12$")
        bill=12
    else:
        print("pay 5$")
        bill=5
    photo=input("do you want a photo taken enetr y or n:")
    if photo=="y":
        bill +=3
    print("u can ride")
else:
    print("u cant ride")

print(f"your bill is :{bill}")