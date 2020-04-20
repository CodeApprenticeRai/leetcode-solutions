class Solution:
    def countElements(self, arr: List[int]) -> int:
        cache = {}

        for num in arr:
            if num not in cache:
                cache[num] = True

        count = 0
        for num in arr:
            if (num + 1) in cache:
                count += 1
        return count