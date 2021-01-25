def switchTurn(_turn):
    if _turn == "X":
        return "O"
    else:
        return "X"

def makeMove(_turn, _board):
    message = 'enter the coordinates of your move (0 -> 2, both up to down and left to right) as ## (or, "22", for example): '
    try: 
        _move = input(message)
        if len(_move) > 2:
            print("Invalid entry, try again")
            makeMove(_turn, _board)
        else:
            _board[int(_move[0])][int(_move[1])] = _turn
    except IndexError:
        print("Invalid entry, try again")
        makeMove(_turn, _board)
    except KeyboardInterrupt:
        print("okay, bye!")
        quit()

def checkHorizontalWin(_board):
    for row in _board:
        if '-' not in row:
            if row[0] == row[1] and row[1] == row[2]:
                return True
    return False

def checkVerticleWin(_board):
    i = 0 #for col
    j = 0 #for row
    while j < len(_board):
        temp = [_board[i][j],_board[i+1][j],_board[i+2][j]]
        if '-' not in temp:
            if temp[0] == temp[1] and temp[1] == temp[2]:
                return True
        j+=1
    return False

def checkDiagWin(_board):
    negSlope = [_board[0][0],_board[1][1],_board[2][2]]
    posSlope = [_board[2][0],_board[1][1],_board[0][2]]
    if "-" not in negSlope:
        if negSlope[0] == negSlope[1] and negSlope[1] == negSlope[2]:
            return True
    if "-" not in posSlope:
        if posSlope[0] == posSlope[1] and posSlope[1] == posSlope[2]:
            return True
    return False
