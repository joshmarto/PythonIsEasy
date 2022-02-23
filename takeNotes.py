# Note Taking
filename = input("Enter the file name: ")
try:
    file = open(filename)
    file.close()
    option = int(input("Select between the following options (select the number): \n1. Read the file \n2. Delete the file and start over \n3. Append the file \n4. Replace a single line\n"))
    if option == 1:
        file = open(filename, "r")
        print(file.read())
        file.close()
    elif option == 2:
        file = open(filename, "w")
        newEnter = input("Enter the new content of this note:\n")
        file.write(newEnter)
        file.close()
    elif option == 3:
        file = open(filename, "a+")
        addEnter = input("Enter what you would like to append to the note:\n")
        file.write(f"\n{addEnter}")
        file.close()
    elif option == 4:
        file = open(filename, "r")
        lineR = int(input("Enter the line you want to replace\n"))
        text = input("Enter the new text you want to have there\n")
        fileLines = file.read().split("\n")
        fileLines[lineR] = text
        file.close()
        file = open(filename, "w")
        for line in fileLines:
            file.write(line + "\n")
        file.close()
except IOError:
    print("New file created")
    file = open(filename, "w")
    enter = input("Enter the content of the file\n")
    file.write(enter)
    file.close()
finally:
    file.close()
