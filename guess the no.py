import random
number=random.randrange(1,50)
guess=int(input("guess a number between 1 and 50="))
while guess!=number:
    if guess<number:
        print("guess a greater number.Try again")
        guess=int(input("\nguess a number between 1 and 50"))
    else:
        print("guess a smaller number.Try again")
        guess=int(input("\nguess a number between 1 and 50"))
print("you guess the number correctly!")          
