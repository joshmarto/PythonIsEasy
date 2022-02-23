# Tic-Tac-Toe
def drawField(field):
    for row in range(5):
        if row % 2 == 0:
            practicalRow = int(row / 2)
            for column in range(5):
                if column % 2 == 0:
                    practicalColumn = int(column / 2)
                    if column != 4:
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end="")
        else:
            print("-----")

player = 1
field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawField(field)
while (True):
    print("Player turn ", player)
    moveRow = int(input("Please enter the row: "))
    moveColumn = int(input("Please enter the column: "))
    if player == 1:
        if field[moveColumn][moveRow] == " ":
            field[moveColumn][moveRow] = "X"
            player = 2
    else:
        if field[moveColumn][moveRow] == " ":
            field[moveColumn][moveRow] = "O"
            player = 1
    drawField(field)
