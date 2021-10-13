def drawField(field):
    for row in range(11):
        if row % 2 == 0:
            practicalRow = int(row / 2)
            for column in range(13):
                if column % 2 == 0:
                    practicalColumn = int(column / 2)
                    if column != 12:
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end="")
        else:
            print("-------------")
def setWinner(field, space):
    #Horizontal verification
    for c in range(3):
        for r in range(6):
            if field[r][c] == space and field[r][c+1] == space and field[r][c+2] == space and field[r][c+3] == space:
                return True;
    #Vertical verification
    for c in range(6):
        for r in range(5):
            if field[r][c] == space and field[r+1][c] == space and field[r+2][c] == space and field[r+3][c] == space:
                return True;
    #Negative diagonal verification
    for c in range(4):
        for r in range(4):
            if field[r][c] == space and field[r+1][c+1] == space and field[r+2][c+2] == space and field[r+3][c+3] == space:
                return True;
    #Positive diagonal verification
    for c in range(3):
        for r in range(3, 7):
            if field[r][c] == space and field[r-1][c+1] == space and field[r-2][c+2] == space and field[r-3][c+3] == space:
                return True;
    
    


player = 1
field = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    ]
drawField(field)
winner = 0
stop = False
Rows = [5, 5, 5, 5, 5, 5, 5]
while (not stop):
    print("Player turn ", player)
    moveColumn = int(input("Please enter the column: "))
    moveRow = Rows[moveColumn]
    if player == 1:
        if field[moveColumn][moveRow] == " ":
            field[moveColumn][moveRow] = "X"
            Rows[moveColumn] -= 1
            if (setWinner(field, field[moveColumn][moveRow])):
                winner = player
                drawField(field)
                print(f"Player {winner} (x) wins!")
                input()
                break;
            player = 2
    else:
        if field[moveColumn][moveRow] == " ":
            field[moveColumn][moveRow] = "O"
            Rows[moveColumn] -= 1
            if (setWinner(field, field[moveColumn][moveRow])):
                winner = player
                drawField(field)
                print(f"Player {winner} (O) wins!")
                input()
                break;
            player = 1
    drawField(field)
