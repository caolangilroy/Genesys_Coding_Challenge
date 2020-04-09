import numpy as np

class FiveInARow:

    num_players = 0
    count = 0
    _players = []
    grid = None
    def __init__(self):
        self._gameOver = False
        self._is_started = False
        self.winner = None
        self.turn = 1
        self.grid = np.full((6, 9), "( )")

    player1Move = 0
    player2Move = 0


    def takeTurn(self, playerMove):
        print(f"You have selected column {playerMove}")
        if 0 < playerMove < 10:
            playerMove = playerMove - 1
            self.updateGrid(playerMove)


    def setP1Token(self, tokenChoice):
        if tokenChoice == 1:
            self.p1Token = "(X)"
            self.p2Token = "(O)"

        else:
            self.p1Token = "(O)"
            self.p2Token = "(X)"

    def updateGrid(self, move):
        token = None
        if self.turn == 1:
            token = self.p1Token
            opponentToken = self.p2Token
        else:
            token = self.p2Token
            opponentToken = self.p1Token

        row = 5
        while self.grid[row][move] == token or self.grid[row][move] == opponentToken:
            if row == 0:
                print("This Row is full! Choose another Row.")

                # self.makeMove(move)

                break
            else:
                row = row - 1

        self.grid[row][move] = token
        # ROW is where the token is
        print(self.grid[row][move])
        print(self.grid)
        freeSlots = 0
        self.checkForWin(token, row, move)

        print("Free slots: " + str(freeSlots))

    def checkForWin(self, token, row, col):
        self.checkHorizontal(token, row, col)
        self.checkVertical(token, row, col)
        self.checkDiagonalLeftRightDown(token, row, col)
        self.checkDiagonalLeftRightUp(token, row, col)

    def checkHorizontal(self, token, row, col):
        number_of_matches = 1
        currentRow = row
        currentCell = col

        # go left
        leftCell = currentCell - 1
        if leftCell != -1:
            while True:
                if self.grid[currentRow][leftCell] == token:
                    number_of_matches = number_of_matches + 1
                    leftCell = leftCell - 1
                    if leftCell == -1:
                        break
                else:
                    break
        rightCell = currentCell + 1

        # Go Right
        if rightCell != 9:
            while True:
                if self.grid[currentRow][rightCell] == token:
                    number_of_matches = number_of_matches + 1
                    rightCell = rightCell + 1
                    if rightCell == 9:
                        # Need to break because 9 will cause an exception in the numpy array
                        break
                else:
                    break

        if number_of_matches == 5:
            self.winner = self.turn
            self._gameOver = True

    def checkVertical(self, token, row, col):
        number_of_matches = 1
        currentRow = row
        currentCell = col

        # check below
        rowBelow = currentRow + 1
        if rowBelow != 6:
            while True:
                print(f'row {rowBelow} --- col {currentCell}')
                print(self.grid[rowBelow][currentCell])
                if self.grid[rowBelow][currentCell] == token:
                    number_of_matches = number_of_matches + 1
                    rowBelow = rowBelow + 1
                    if rowBelow == 6:
                        break
                else:
                    break

        if number_of_matches == 5:
            self.winner = self.turn
            self._gameOver = True

    def checkDiagonalLeftRightDown(self, token, row, col):
        number_of_matches = 1
        currentRow = row
        currentCell = col

        # go left and down
        rowBelow = currentRow + 1
        leftCell = currentCell - 1
        if leftCell != -1 and rowBelow != 6:
            while True:
                if self.grid[rowBelow][leftCell] == token:
                    number_of_matches = number_of_matches + 1
                    leftCell = leftCell - 1
                    rowBelow = rowBelow + 1
                    if leftCell == -1 or rowBelow == 6:
                        break
                else:
                    break

        # Go Right and up
        rightCell = currentCell + 1
        rowAbove = currentRow - 1
        if rightCell != 9 and rowBelow != -1:
            while True:
                if self.grid[rowAbove][rightCell] == token:
                    number_of_matches = number_of_matches + 1
                    rightCell = rightCell + 1
                    rowAbove = rowAbove - 1
                    if rightCell == 9 or rowAbove == -1:
                        # need to break because 9 or -1 indexes will cause an exception in the numpy array
                        break
                else:
                    break

        if number_of_matches == 5:
            self.winner = self.turn
            self._gameOver = True

    def checkDiagonalLeftRightUp(self, token, row, col):
        number_of_matches = 1
        currentRow = row
        currentCell = col

        # go left and up
        rowAbove = currentRow - 1
        leftCell = currentCell - 1
        if leftCell != -1 and rowAbove != -1:
            while True:
                if self.grid[rowAbove][leftCell] == token:
                    number_of_matches = number_of_matches + 1
                    leftCell = leftCell - 1
                    rowAbove = rowAbove - 1
                    if leftCell == -1 or rowAbove == -1:
                        break
                else:
                    break

        # Go Right and Down
        rightCell = currentCell + 1
        rowBelow = currentRow + 1
        if rightCell != 9 and rowBelow != 6:
            while True:
                print(self.grid[rowBelow][rightCell])
                if self.grid[rowBelow][rightCell] == token:
                    number_of_matches = number_of_matches + 1
                    rightCell = rightCell + 1
                    rowBelow = rowBelow + 1
                    if rightCell == 9 or rowBelow == 6:
                        # Need to break because indexes 9 and 6 will cause an exception in the numpy array
                        break
                else:
                    break

        if number_of_matches == 5:
            self.winner = self.turn
            self._gameOver = True

    def setWinner(self, playerNum):
        self.winner = playerNum
        self._gameOver = True
        return playerNum

    def print_board(self):
        print(f'GRID -> \n {self.grid}')
        board_string = ''
        for x in range(6):
            board_string += f'{str(self.grid[x][:])}\n'
        print(str(board_string))
        return board_string

    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def is_over(self):
        return self._gameOver

    def is_started(self):
        return self._is_started

    def add_player(self, name):
        self._players.append(name)
        self.num_players += 1
        if self.num_players == 2:
            self._is_started = True
            print('GAME STARTED!!!')



if __name__ == "__main__":
    grid = np.full((6, 9), "( )")
    grid[5][0] = '(x)'
    print(str(grid[0][:]))
    print(grid[1][:])
    print(grid[2][:])
    print(grid[3][:])
    print(grid[4][:])

