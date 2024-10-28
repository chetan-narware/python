import art
print(art.cal)
def add(n1,n2):
    return n1+n2

def mul(n1,n2):
    return n1*n2

def sub(n1,n2):
    return n1-n2

def div(n1,n2):
    return n1/n2

def calculator():
    num1=float(input("enter the no.1: "))
    num2=float(input("enter the no.2: "))
    op = input("enter the operation to be performed in the form of +,-,*,/: ")
    dic={"+":add,"-":sub,"*":mul,"/":div}
    calculation_function= dic[op]
    res=calculation_function(num1,num2)
    print(f"{num1}{op}{num2}={res}")
    q=input("enter y to continue and r to reset and n to stop: ")
    if q=="y":
        cnt=True
    elif q=="r":
        calculator()
    else:
        cnt=False
    while cnt:
        op = input("enter the operation to be performed in the form of +,-,*,/: ")
        nw= float(input("enter the new number: "))
        calculation_function= dic[op]
        res2=calculation_function(res,nw)
        print(f"{res}{op}{nw}={res2}")
        res=res2
        q=input("enter y to continue and r to reset and n to stop: ")
        if q=="y":
            cnt=True
        elif q=="r":
            calculator()
        else:
            cnt=False
    exit
calculator()
