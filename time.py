#IMPORT 2
import time

currentTime = time.perf_counter()
print("Hello", end="")
print(", world!")
pastTime = time.perf_counter()
print(pastTime - currentTime)

"""
print("1")
time.sleep(1)
print("2")
"""

for i in range(1, 11):
    print(i)
    time.sleep(1)

