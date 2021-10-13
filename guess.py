#GUESSING GAME
from random import randint

rnd = randint(0, 100)

while (True):
    guess = int(input("Enter your guess: "))
    if guess == rnd:
        break
    elif guess < rnd:
        print("Your guess was too low")
    else:
        print("Your guess was too high")
print(f"You guess correctly with {rnd}")
