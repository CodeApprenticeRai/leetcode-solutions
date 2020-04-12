'''
    We have a collection of stones.
    Each stone has a positive integer weight.
    Each turn we choose the two heaviest stones and smash them together.
    Suppose the stones have weights x and y, with x <= y.
    The result of this smash is:
        x == y -> both stones ar edestryoed
        x != y -> the stone of weight x is totally destroyed and the stone of weight y  has new
        weight y -x,

        At the end there is at msot 1 stone left. Return the weight of this stone or 0 if there are no stones
'''


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if (len(stones) == 1):
            return stones[0]

        queue = []

        for num in stones:
            heapq.heappush(queue, -1 * num)

        while (len(queue) > 1):
            y = heapq.heappop(queue) * -1
            x = heapq.heappop(queue) * -1
            if (y > x):
                heapq.heappush(queue, -1 * (y - x))

        return 0 if (len(queue) == 0) else queue[0] * -1