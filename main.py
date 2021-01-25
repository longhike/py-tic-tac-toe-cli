from board import Board
from logic import *

def main():
    done = False
    turn = "O"
    game_board = Board()
    board = game_board.board
    while not(done):
        if checkHorizontalWin(board) or checkVerticleWin(board) or checkDiagWin(board):
            game_board.show(board)
            print(turn + " WINS!!!!!")
            done = True
        else:
            turn = switchTurn(turn)
            game_board.show(board)
            makeMove(turn, board)
    quit()

if __name__ == "__main__":
    main()



