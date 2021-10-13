#INTRODUCTION TO IMPORTING
import random as r
#from random import *

r.seed(1)
randInt = r.randint(0, 10) #Start<=n<=End
print(randInt)

randFloat = r.random() #0.0<=n<1.0
print(randFloat)

randUniform = r.uniform(1, 1100) #start<=n<=end
print(randUniform)

#ALTERNATIVE IMPORT METHODS
simpleList = [1, 3, 5, 7, 11]
pickElement = r.choice(simpleList)

print(simpleList)
r.shuffle(simpleList)
print(simpleList)
