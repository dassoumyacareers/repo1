import random
answer=random.randint(1,10)
guess=0
print("guess a number between 1 to 10: ")
while guess!=answer:
    guess=int(input())
    if guess==0:
        break
    if guess==answer:
        print("you guessed it correctly")
        break
    else:
        if guess<answer:
            print("guess higher")
        else:
            print("guess lower")
