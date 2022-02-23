# SHAPES
Length = 10
toPrint = input("Enter the character to print: ")
for pos in range(1, Length+1):
    print(toPrint*pos)

for pos in range(Length-1, 0, -1):
    print(toPrint*pos)