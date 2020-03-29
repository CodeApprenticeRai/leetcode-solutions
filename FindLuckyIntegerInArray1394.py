import heapq


class Solution:
    def findLucky(self, arr):
        arr_sorted = []
        count_memo = {}

        for num in arr:
            if num not in count_memo:
                count_memo[num] = 1
                heapq.heappush(arr_sorted, -1 * num)
            else:
                count_memo[num] += 1

        while (len(arr_sorted) > 0):
            num = -1 * heapq.heappop(arr_sorted)
            if (num == count_memo[num]):
                return num
        return -1