myUniqueList = []
myLeftovers = []

def add(element):
    if not element in myUniqueList:
        myUniqueList.append(element)
        return True
    else:
        myLeftovers.append(element)
        return False

add("Jack")
add("Ryan")
add("Mark")
add("Jack")
add("Peter")
add("Mark")
add("Martin")
add("Steve")
add("Steve")
print("This is My Unique List:")
for element in myUniqueList:
    print(element)
print("This is my Leftovers: " + str(myLeftovers))
for element in myLeftovers:
    print(element)
