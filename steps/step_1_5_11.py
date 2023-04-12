class Cell:
    def __init__(self, around_mines, mine=0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell(around_mines, mine)] * N for i in range(N)]
        #randrange(0, self.N)
    def show():
