# FUNCTIONS
def addNum(number):
    number += 1
    return number
testVariable = 0
testVariable = addNum(testVariable)
print(testVariable)

def addMore(times, add):
    output = 0
    for i in range(times):
        output += add
        print(output)

t = int(input("Enter the times: "))
a = int(input("Enter the steps: "))
addMore(t, a)
