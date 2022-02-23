#GUESS 2
from random import random
from time import perf_counter

rnd = random()
upper = 1.0
lower = 0.0
#guess = 0.5 -> Too low -> lower = 0.5
#guess = 0.9 -> Too high - upper = 0.9
"""guess = 0.5 #Not quite necessary"""

start = perf_counter()
while(True):
    guess = (upper + lower) / 2
    if guess == rnd:
        break
    elif guess < rnd:
        lower = guess
    else:
        upper = guess
end = perf_counter()
print(f"PC catched it with {guess}")
print(f"It took {end - start} seconds to catch it")
