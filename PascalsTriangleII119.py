'''
    Given a non-negative index k where k<= 33, return the kth index row of the pascal traingl
        0 1 2
    0 : 1
    1 : 1 1
    2 : 1 2 1
    3 : 1 3 3 1
    4 : 1 4 6 4 1

'''


class Solution:
    def __init__(self):
        self.table = [[1]]

        #
        for i in range(0, 34):
            #
            row = [1]

            #
            j = 1
            while (j < (i + 1)):
                row.append(self.table[-1][j - 1] + self.table[-1][j])
                j += 1

            #
            row.append(1)

            self.table.append(row)
        return None

    def getRow(self, row_index: int) -> List[int]:
        return self.table[row_index]