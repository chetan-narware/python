print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
comb=name1+name2
comb=comb.lower()
t = comb.count("t")
r=comb.count("r")
u=comb.count("u")
e=comb.count("e")
l=comb.count("l")
o=comb.count("o")
v=comb.count("v")
e=comb.count("e")
s=(t+r+u+e)*10+(l+o+v+e)


if s<10 or s>90:
  print(f"Your score is {s}, you go together like coke and mentos.")
elif s>=40 and s<=50:
  print(f"Your score is {s}, you are alright together.")
else:
  print(f"Your score is {s}.")

  