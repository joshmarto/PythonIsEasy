class Pet:
    def __init__(self, n, a, h, p):
        self.name = n
        self.age = a
        self.hunger = h
        self.playFul = p
    #Getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playFul
    #Setters
    def setName(self, n):
        self.name = n

    def setAge(self, a):
        self.age = a

    def setHunger(self, h):
        self.hunger = h

    def setPlayful(self, p):
        self.playFul = p

    def __str__(self):
        return (self.name + " is " + str(self.age) + " years old")

class Human:
    def __init__(self, name, pets):
        self.name = name
        self.pets = pets

    def hasPets(self):
        if len(self.pets) != 0:
            return "Yes"
        else:
            return "No"

pet1 = Pet("Jim", 3, False, True)
print(pet1.getName())
print(pet1.getPlayful())
pet1.setName("Snowball")
print(pet1.getName())
print(pet1.name)

class Dog(Pet):
    def __init__(self, name, age, hunger, playful, breed, toy):
        Pet.__init__(self, name, age, hunger, playful)
        self.breed = breed
        self.favoriteToy = toy

    def wantsToPlay(self):
        if self.playFul == True:
            return ("Dog wants to play with " + self.favoriteToy)
        else:
            return "The dog doesn't want to play"

class Cat(Pet):
    def __init__(self, name, age, hunger, playful, place):
        Pet.__init__(self, name, age, hunger, playful)
        self.favoritePlaceToSit = place

    def wantsToSit(self):
        if self.playFul == False:
            print("Cat wants to sit in", self.favoritePlaceToSit)
        else:
            print("The cat wants to play")

    def __str__(self):
        return (self.name + " likes to sit in " + self.favoritePlaceToSit)

husky = Dog("Snowball", 5, False, True, "Husky", "Stick")
play = husky.wantsToPlay()
print(play)

Mish = Cat("Fluffy", 3, False, False, "the sun ray")
Mish.wantsToSit()
print(Mish)

Alice = Human("Alice", [husky, Mish])
hasPet = Alice.hasPets()
print(hasPet)
print(Alice.pets[0])




