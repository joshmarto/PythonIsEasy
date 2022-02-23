"""
   File I/O
   open("filename", "action")
   between the possible actions are:
   - r (read)
   - w (write)
   - a (append)
   - r+ (read & write)
"""
#File = open("Filename", "r")
#File.close()

vacationSpots = ["London", "Paris", "New York", "Manila", "Honolulu"]
vacationFile = open("vacationPlaces", "w")

for spot in vacationSpots:
    vacationFile.write(str(spot) + "\n") # Just string can be passed as parameter

vacationFile.close()
vacationFile = open("vacationPlaces", "r")
# 1 option to print
firstLine = vacationFile.readline()
print(firstLine)
secondLine = vacationFile.readline()
print(secondLine)
for line in vacationFile:
    print(line, end="")
print("-----------DIVISON-----------")
# 2 option to print
"""theWholeFile = vacationFile.read()
print(theWholeFile)"""
vacationFile.close()

finalSpot = "Thailand"
vacationFile = open("vacationPlaces", "a")
vacationFile.write(finalSpot)
vacationFile.close()

vacationFile = open("vacationPlaces", "r")
for line in vacationFile:
    print(line, end="")
vacationFile.close()


print("")
print("-----------ANOTHER DIVISION-----------")
for i in range(5):
    with open("vacationPlaces"+str(i), "r") as vacationFile: # Use of the file without need to open/close
        for line in vacationFile:
            print(line, end="")
