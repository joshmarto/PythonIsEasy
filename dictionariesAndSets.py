# Dictionaries and Sets
sets = {"element 1", "element 2", "element 3", "element 4", "element 1"} # sets remove repeated elements
print(sets)
if "element 1" in sets:
    print("yes")

countryList = []
for i in range(5):
    country = input("Please enter your country: ")
    countryList.append(country)
countrySet = set(countryList)
print(countryList)
print(countrySet)

Dictionary = {"Key": "Value", "Key 2":"Value 2", "Key 3":"Value 3"}

countryDictionary = {}
for country in countryList:
    if country in countryDictionary:
        countryDictionary[country] += 1
    else:
        countryDictionary[country] = 1
print(countryDictionary)
