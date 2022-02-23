class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0

    #Setters
    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model
        
    def setYear(self, year):
        self.year = year

    def setWeight(self, weight):
        self.weight = weight

    #Getters
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model
    
    def getYear(self):
        return self.year

    def getWeight(self):
        return self.weight

    def Repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False


class Cars(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = False

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True
        self.isDriving = False


class Planes(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = False

    def Flying(self):
        if self.needsMaintenance == False:
            self.isFlying = True
            return True
        else:
            print("The plane can't fly until it's repaired.")
            return False

    def Landing(self):
        self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 99:
            self.needsMaintenance = True
        self.isFlying = False

#Definition
car1 = Cars("BMW", "M3", 2008, 550)
car2 = Cars("Audi", "R8", 2016, 475)
car3 = Cars("Ford", "Explorer", 2020, 725)
try:
    model = input("Enter the model ")
    make = input("Enter the make ")
    year = int(input("Enter the year "))
    weight = int(input("Enter the weight "))
    car1 = Cars(model, make, year, weight)
except Exception as e:
    print(str(e))
finally:
    print("Moving to function...")

plane1 = Planes("Airbus", "Boing 747", 2017, 2600)


#Function
print("CAR")
for i in range(100):
    car1.Drive()
    car1.Stop()
print(f"Trips since maintenance {car1.tripsSinceMaintenance}")
car1.Drive()
car1.Repair()


print("PLANE")
for i in range(100):
    plane1.Flying()
    plane1.Landing()
print(f"Trips since maintenance {plane1.tripsSinceMaintenance}")
print(f"Does the plane 1 can fly: {plane1.Flying()}")
plane1.Repair()
print(f"Does the plane 1 can fly: {plane1.Flying()}")




