#Participant Data
participantNumber = 5
participantData = []
outputFile = open("participantData.txt", "w")

registeredParticipants = 0
while (registeredParticipants < participantNumber):
    tempPartData = []
    name = input("Enter the name: ")
    tempPartData.append(name)
    contry = input("Enter the country of origin: ")
    tempPartData.append(country)
    age = int(input("Enter the age: "))
    tempPartData.append(age)
    participantData.append(tempPartData)
    registeredParticipants += 1

for participant in participantData:
    for data in participant:
        outputFile.write(str(data))
        outputFile.write(" ")
    outputFile.write("\n")
outputFile.close()

inputFile = open("participantData.txt", "r")
inputList = []
for line in inputFile:
    tempParticipant = line.strip("\n").split(" ")
    inputList.append(tempParticipant)

age = {}
for part in inputList:
    tempIf = part[-1]
    if tempIf in age:
        age[tempIf] += 1
    else:
        age[tempIf] = 1
print(age)
countries = {}
for part in inputList:
    tempIf = part[-1]
    if tempIf in countries:
        agcountries[tempIf] += 1
    else:
        countries[tempIf] = 1

oldest = 0
youngest = 100
mostOccurringAge = 0
counter = 0
for tempAge in age:
    if tempAge > oldest:
        oldest = tempAge
    if tempAge < youngest:
        youngest = tempAge
    if age[tempAge] > counter:
        counter = age[tempAge]
        mostOccurringAge = tempAge

print(f"Greatest age is {oldest}")
print(f"Youngest age is {youngest}")
print(f"Most occurring age is {mostOccurringAge} with {counter} participants")

inputFile.close()
