import random
import art
print(art.logo)


word_list = ["avocado", "apple", "sugar"]
x = random.choice(word_list)
print(x)
heart = 6
n = len(x)
guess = ["_"] * n 
end_of_game=False
while not end_of_game:
    s = input("Please guess a letter: ").lower()
    for i in range(n):  
        if x[i] == s: 
            guess[i] = s  
        
    print(guess)
    
    if "_" not in guess:
        end_of_game=True
        print("you win")
    if s not in guess: 
        heart-=1
        print(art.HANGMANPICS[6-heart])
    if heart==0:
        end_of_game=True

