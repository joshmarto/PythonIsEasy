from random import choice
from os import system
from time import sleep

def write(list):
    for i in range(len(list)):
        print(list[i], end=" ")
    print("\n")

def draw(x, word):
    if x == 0:
        print("---|\n|  |\n|    \n|    \n|    \n|    \n|    \n\n")
        write(word)
    elif x == 1:
        print("---|\n|  |\n|  O \n|    \n|    \n|    \n|    \n\n")
        write(word)
    elif x == 2:
        print("---|\n|  |\n|  O \n|  | \n|    \n|    \n|    \n\n")
        write(word)
    elif x == 3:
        print("---|\n|  |\n|  O \n| /| \n|    \n|    \n|    \n\n")
        write(word)
    elif x == 4:
        print("---|\n|  |\n|  O \n| /| \n|  | \n|    \n|    \n\n")
        write(word)
    elif x == 5:
        print("---|\n|  |\n|  O \n| /| \n|  | \n| /  \n|    \n\n")
        write(word)
    elif x == 6:
        print("---|\n|  |\n|  O \n| /|\\ \n|  | \n| /  \n|    \n\n")
        write(word)
    elif x == 7:
        print("---|\n|  |\n|  O \n| /|\\ \n|  | \n| / \\  \n|    \n\n")
        write(word)

print("Welcome to Hangman!")
finish = False
words = ["car", "computer", "batman", "programming", "book", "counter", "games", "elevators", "soccer", "colors", "animals", "loli pop"]
word = input(f"Player 1, please enter the word to guess or enter 'automatic' to pick a random word ")
system('cls')
failed = []
guess = []

if word == "automatic":
    word = choice(words)
for i in range(len(word)):
    guess.append("_")
c = 0

while (not finish):
    print("Failed letters ", end="")
    write(failed)
    draw(c, guess)
    letter = input("Please enter your guess of letter ")
    for x in range(len(word)):
        if letter == word[x]:
            guess[x] = letter
    print("\n")
    if not letter in word:
        failed.append(letter)
        c += 1
    if c > 6:
        draw(c, guess)
        print("You lose")
        break
    if not "_" in guess:
        draw(c, guess)
        print("You won! Congrats!")
        break
    system('cls')
