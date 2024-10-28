print("welcome to tip calculator")
pep=int(input("no. of people:"))
amt=float(input("amout:"))
tip=float(input("tip:10,12,15 $:"))

tamt=amt + amt*tip/100
amt_per_person=tamt/pep

final_amt=round(amt_per_person,2)

print(f"each person will have to pay:{final_amt}$")