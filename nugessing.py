import random
def gen_num():
    i=random.randint(1,100)
    return i

def game(num,attempts):
    gameon=True
    while gameon and attempts!=0:
        gess=int(input("what is the Number that i am thinking of: "))
        attempts-=1
        diff=abs(gess-num)
        if diff==0:
            print(f"you got it right i was thinking about {num}!!!!!!")
            gameon=False
        elif diff>10:
            print("too far")
        elif diff<10:
            print("less far")
        elif diff<5:
            print("very close")
        print(f"you have {attempts} attempts left.")
        if attempts==0:
            print(f"you lose the number was {num}.....")

print("GUESS THE NUMBER THAT I AM THINKING OF")
mode=input("game mode: hard/easy: ")
if mode=='hard':
    attmp=5
else:
    attmp=10

num=gen_num()
game(num,attmp)