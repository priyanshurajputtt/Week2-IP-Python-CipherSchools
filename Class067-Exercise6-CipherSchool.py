import random
win_num=random.randint(1,100)
num=int(input("guess a number between 1 and 100 : "))
guess=1
game_over=False

while not game_over:
    if num==win_num:
        print(f"you win an you guess this num in {guess} time.")
        game_over=True
    else:
        if num<win_num:
            print("too low")
            guess+=1
            num=int(input("Guess again: "))
        else:
            print("too high")
            guess+=1
            num=int(input("Guess again: "))