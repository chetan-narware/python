def function_name(fname,lname):
     fname=fname.title()
     lname=lname.title()
     return f"{fname}{lname}"

fname=input()
lname=input()

print(function_name(fname,lname))