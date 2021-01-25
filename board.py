class Board: 
    def __init__(self, board=[["-","-","-"],["-","-","-"],["-","-","-"]]):
        self.board = board
    
    def show(self, _board):
        for _row in _board:
            print(_row)