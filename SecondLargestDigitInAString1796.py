class Solution:
    def secondHighest(self, s: str) -> int:
        cache = set()
        heap = []
        for char in s:
            if char.isdigit() and (char not in cache):
                cache.add(char)
                heapq.heappush(heap, -1*int(char))
        if (len(heap) >= 2):
            heapq.heappop(heap)
            return -1 * heapq.heappop(heap)
        else:
            return -1