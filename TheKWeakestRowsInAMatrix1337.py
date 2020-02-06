'''
    Given an m*n matrix mat of ones  ( reprsenting soliders )
    and zeros ( representing civilians ), return the indexes of the k weakest rows in the matrixs ordered from weakest to strongest

    Approach:
        Sort the rows in the order of decreasing sum, where rows

    Start with a dict < key, value > :: where the key is the sum of the row, and the value is a list of rows with that sum
    We iterate the matrix in order to populate this dict (  let it be wrapped by a pq( ) just to make accessing it a little easier ).

    Return the first K elements we get from removing elements from our pq-dict structure
'''

from heapq import heappush, heappop


class Solution:
    def kWeakestRows(self, mat, k):
        heap = []
        sum_to_row = {}

        # compute sum for each row and store in order-preserving data structure
        for i in range(len(mat)):
            row_sum = sum(mat[i])

            if row_sum not in sum_to_row:
                sum_to_row[row_sum] = [i]
                heappush(heap, (row_sum, sum_to_row[row_sum]))
            else:
                sum_to_row[row_sum].append(i)

        k_weakest_rows = []
        heap_node = None
        _i = None
        while (k > 0):
            if ((heap_node == None) or (_i >= len(heap_node[1]))):
                heap_node = heappop(heap)
                _i = 0

            k_weakest_rows.append(heap_node[1][_i])
            _i += 1
            k -= 1

        return k_weakest_rows