class Game:

    def __init__(self):
        self.board = [['.' for _ in range(3)] for _ in range(3)]


    def printBoard(self):
        for row in self.board:
            print(row)


    def place(self, char, row, col):
        if self.board[row][col] == '.':
            self.board[row][col] = char


    def isWinner(self):
        return None
    

g = Game()

while not g.isWinner():
    p1r = int(input("player 1: "))
    p1c = int(input("player 1: "))  
    
    g.place('x', p1r, p1c)
    g.printBoard()
    
    p2r = int(input("player 1: "))
    p2c = int(input("player 1: "))  

    g.place('o', p2r, p2c)
    g.printBoard()
    
