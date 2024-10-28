import random


def dealer():
    list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    i = random.randint(0,12)
    return list[i]

def dealing_cards(player_cards):
    card=dealer()
    player_cards.append(card)


def sum(list):
    s=0
    for x in list:
        s+=x
    return s


player_ans=input("Do You Want To Play BlackJack? Answer Y/N: ")
player_ans=player_ans.lower()

while player_ans=='y':
    player_cards=[]
    for i in range(2):
        dealing_cards(player_cards)
    print("your cards are")
    print(player_cards)
    dealers_card=[]
    for i in range(2):
        dealing_cards(dealers_card)
    print(f"dealers cards are:{dealers_card[0]} and  a hidden card")
    players_call=input("Do You Want Another Card? Y/N: ")
    players_call=players_call.lower()
    if players_call=='y':
        dealing_cards(player_cards)
        print("your new cards are")
        print(player_cards)
    if sum(player_cards)>21:
        if 11 in player_cards:
            player_cards.remove(11)
            player_cards.append(1)
            print("your new cards are")
            print(player_cards)
    if sum(player_cards)>21:
        print("You Have Been Busted")
    else:
        print(f"dealers cards are:\n{dealers_card}")
        if sum(dealers_card)<17:
            dealing_cards(dealers_card)
            print(f"new dealers cards are (dealer have been give an additional card):\n{dealers_card}")
        if sum(player_cards)== sum(dealers_card):
            print("Game Has Been Drawn")
        elif sum(player_cards)>sum(dealers_card):
            print("You Won!!!")
        else:
            print("(-_-) You Lose (-_-)")
    player_ans=input("Do You Want To Play BlackJack? Answer Y/N: ")
    player_ans=player_ans.lower()


print("!!!!!THANK YOU FOR LOSING MONEY TO US!!!!!")

    