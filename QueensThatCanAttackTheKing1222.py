'''
    From the cell of the king
    Iterate through the series of cell that would represent all
    neighboring cells of the king

    We want to step from cell to cell in that direction until we
    reach a queen or we reach a cell that doesn't exist within the
    board.

    if we reach a queen, we add that queen to our our list,
    if we reach a cell that is outside of the board, then we just return

'''


class Solution:
    def queensAttacktheKing(self, queens, king):
        # utility to make it simple to calculate relative cell indices
        self.directions = {
            "N": (0, -1), "NE": (1, -1),
            "E": (1, 0), "SE": (1, 1),
            "S": (0, 1), "SW": (-1, 1),
            "W": (-1, 0), "NW": (-1, -1),
        }

        # cache queen positions for O(1) checking if queen is in a cell
        self.queenCells = self.cacheQueenCells(queens)

        self.queensThatCanAttackKing = []

        for direction in self.directions:
            self.checkDirectionForQueen(direction, self.getNextIndex(direction, king))

        return self.queensThatCanAttackKing

    def cacheQueenCells(self, queens):
        queenCells = {}

        for queenCell in queens:
            if queenCell[0] not in queenCells:
                queenCells[queenCell[0]] = {}
            queenCells[queenCell[0]][queenCell[1]] = True

        return queenCells

    # check if current cell is either out of bounds or has queen in it
    def checkDirectionForQueen(self, direction, currentIndex):
        if not self.cellInsideChessboard(currentIndex):
            return None
        elif self.cellContainsQueen(currentIndex):
            self.queensThatCanAttackKing.append(currentIndex)
        else:
            nextIndex = self.getNextIndex(direction, currentIndex)
            self.checkDirectionForQueen(direction, nextIndex)
        return None

    def cellInsideChessboard(self, currentIndex):
        return False if (
                (currentIndex[0] < 0) or
                (currentIndex[0] > 7) or
                (currentIndex[1] < 0) or
                (currentIndex[1] > 7)
        ) else True

    def cellContainsQueen(self, currentIndex):
        return False if (
                (currentIndex[0] not in self.queenCells) or
                (currentIndex[1] not in self.queenCells[currentIndex[0]])
        ) else True

    def getNextIndex(self, direction, currentIndex):
        translation = self.directions[direction]
        return (currentIndex[0] + translation[0], currentIndex[1] + translation[1])

    '''
        Critical points: 
            - somewhat inconsistent use of the words cell and index
            - camelCase :/
    '''