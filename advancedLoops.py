import subprocess
import os

os.system("start cmd /c mode con: cols=150 lines=40")

width, height = 40, 150

def Draw(rows, columns):
    for row in range(rows):
        if row%2 == 0:
            for column in range(1, columns+1):
                if column%2 == 1:
                    if column != columns:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print("|", end="")
        else:
            for column in range(1, columns+1):
                if column != columns:
                    print("-", end="")
                else:
                    print("-")
    if rows < height or columns < width:
        return True
    else:
        return False

rows = int(input("Enter the rows: "))
columns = int(input("Enter the columns: "))
Draw(rows, columns)
